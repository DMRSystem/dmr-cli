
from dmr.controller.setup.behavior.osx.step.mixxx_downloader import MixxxDownloader
from dmr.utils.logging.logging_adapter import ILoggingAdapter
from dmr.utils.requests.requests_adapter import RequestsAdapter
from pathlib import Path

import unittest
from mockito import mock, verify, when


class MixxxDownloaderTest(unittest.TestCase):

    def setUp(self):
        self.logger: ILoggingAdapter = mock()
        self.download_url: str = 'mock_url'
        self.download_file_path: Path = mock(Path)
        self.download_file_path._parts = ['mock_path']
        self.download_file_name: str = 'mock_file_name'
        self.requests_adapter: RequestsAdapter = mock()

        when(self.download_file_path).mkdir(parents=True, exist_ok=True).thenReturn(self.download_file_path)

        self.downloader: MixxxDownloader = MixxxDownloader(logging_adapter=self.logger,
                                                           download_url=self.download_url,
                                                           download_file_path=self.download_file_path,
                                                           download_file_name=self.download_file_name,
                                                           requests_adapter=self.requests_adapter)

    def test_downloader_ensures_directory_exists(self):
        self.downloader.execute()

        verify(self.download_file_path).mkdir(parents=True, exist_ok=True)

    def test_downloader_calls_requests_adapter(self):

        self.downloader.execute()
        full_download_path = Path(self.download_file_path, self.download_file_name)
        verify(self.requests_adapter).download_file_to_directory(self.download_url, full_download_path)
