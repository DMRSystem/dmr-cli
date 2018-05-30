
from dmr.utils.requests.requests_adapter import RequestsAdapter
from dmr.utils.logging.logging_adapter import ILoggingAdapter
from dmr.controller.setup.setup_step import ISetupStep, AbstractSetupStepDecorator

from pathlib import Path
import sys


class MixxxDownloader(ISetupStep):

    def __init__(self, **kwargs):
        self.download_url: str = kwargs['download_url']
        self.download_file_path: Path = kwargs['download_file_path']
        self.download_file_name: str = kwargs['download_file_name']
        self.requests_adapter: RequestsAdapter = kwargs['requests_adapter']
        self.logger: ILoggingAdapter = kwargs['logging_adapter']

    def execute(self, depth: int = 0):
        self.logger.info('Downloading Mixxx ({0}) ...'.format(self.download_file_name), 'yellow', indentation=depth)
        self._ensure_download_directory_exists()
        full_download_path: Path = Path(self.download_file_path, self.download_file_name)
        self.requests_adapter.download_file_to_directory(self.download_url, full_download_path)
        self.logger.info('Mixxx downloaded to {0}'.format(full_download_path), indentation=depth)

    def _ensure_download_directory_exists(self):
        self.download_file_path.mkdir(parents=True, exist_ok=True)


class AlreadyDownloadedCheckDecorator(AbstractSetupStepDecorator):

    def __init__(self, setup_step: ISetupStep, full_download_path: Path, logging_adapter: ILoggingAdapter):
        AbstractSetupStepDecorator.__init__(self, setup_step)
        self.full_download_path = full_download_path
        self.logger: ILoggingAdapter = logging_adapter

    def execute(self, depth: int = 0):
        if self.full_download_path.exists():
            self.logger.info('Mixxx image already downloaded at {0}'.format(self.full_download_path), 'blue', depth)
            self.logger.info('Skipping download.', indentation=depth)
            return
        AbstractSetupStepDecorator.execute(self)




