
from dmr.controller.setup.setup_step import ISetupStep
from dmr.utils.logging.logging_adapter import ILoggingAdapter
from pathlib import Path


class MixxxDownloadRemover(ISetupStep):

    def __init__(self, full_download_path: Path, logging_adapter: ILoggingAdapter):
        self.full_download_path = full_download_path
        self.logger = logging_adapter

    def execute(self, depth: int = 0) -> None:
        self.logger.info('Removing mixxx image at {0}'.format(self.full_download_path), 'yellow', indentation=depth)
        self.full_download_path.unlink()
        self.logger.info('Mixxx image removed.', indentation=depth)
