from dmr.controller.setup.behavior.osx.step.mixxx_downloader import MixxxDownloader
from dmr.utils.logging.logging_adapter import ILoggingAdapter

import unittest
from mockito import mock, verify


class MixxxDownloaderTest(unittest.TestCase):

    def setUp(self):
        self.logger: ILoggingAdapter = mock()
        self.download_url = 'mock_url'
        self.download_directory = 'mock_directory'
        self.requests = mock()
        self.downloader: MixxxDownloader = MixxxDownloader(logging_adapter=self.logger,
                                                           download_url=self.download_url,
                                                           download_directory=self.download_directory,
                                                           requests=self.requests)

    def test_downloader_calls_logger(self):
        self.downloader.execute()

        verify(self.logger).info('Downloading Mixxx...')
