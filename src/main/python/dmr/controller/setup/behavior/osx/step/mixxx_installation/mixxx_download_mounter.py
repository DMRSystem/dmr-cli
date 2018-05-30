
from dmr.controller.setup.setup_step import ISetupStep
from dmr.utils.logging.logging_adapter import ILoggingAdapter

from dmr.utils.process.process_adapter import ProcessAdapter

from pathlib import Path


class MixxxDownloadMounter(ISetupStep):

    def __init__(self, logging_adapter: ILoggingAdapter, process_adapter: ProcessAdapter, full_download_path: Path):
        self.logger: ILoggingAdapter = logging_adapter
        self.process_adapter: ProcessAdapter = process_adapter
        self.full_download_path: Path = full_download_path

    def execute(self, depth: int = 0) -> None:
        self.logger.info('Mounting Mixxx image...', 'yellow', indentation=depth)
        self.process_adapter.run(depth, 'hdiutil', 'attach', '-mountpoint', '/Volumes/Mixxx', str(self.full_download_path))
        self.logger.info('Mixxx image mounted.', indentation=depth)
