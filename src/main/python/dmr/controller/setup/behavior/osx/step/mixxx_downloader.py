
from dmr.utils.requests.requests_adapter import RequestsAdapter
from dmr.utils.logging.logging_adapter import ILoggingAdapter
from dmr.controller.setup.setup_step import ISetupStep


class MixxxDownloader(ISetupStep):

    def __init__(self, **kwargs):
        self.download_url: str = kwargs['download_url']
        self.download_directory: str = kwargs['download_directory']
        self.requests_adapter: RequestsAdapter = kwargs['requests_adapter']
        self.logger: ILoggingAdapter = kwargs['logging_adapter']

    def execute(self):
        self.logger.info('Downloading Mixxx...')
