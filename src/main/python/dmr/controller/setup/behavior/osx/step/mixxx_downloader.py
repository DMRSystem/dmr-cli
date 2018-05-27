
import requests
from logging import Logger
from dmr.controller.setup.setup_step import ISetupStep


class MixxxDownloader(ISetupStep):

    def __init__(self, **kwargs):
        self.download_url: str = kwargs['download_url']
        self.download_directory: str = kwargs['download_directory']
        self.requests: requests = kwargs['requests']
        self.logger: Logger = kwargs['logger']

    def execute(self):
        self.logger.info('Downloading Mixxx...')
