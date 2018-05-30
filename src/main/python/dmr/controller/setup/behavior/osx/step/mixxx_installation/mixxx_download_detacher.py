
from dmr.controller.setup.setup_step import ISetupStep
from dmr.utils.logging.logging_adapter import ILoggingAdapter
from dmr.utils.process.process_adapter import ProcessAdapter


class MixxxDownloadDetacher(ISetupStep):

    def __init__(self, logging_adapter: ILoggingAdapter, process_adapter: ProcessAdapter):
        self.logger: ILoggingAdapter = logging_adapter
        self.process_adapter: ProcessAdapter = process_adapter

    def execute(self, depth: int = 0) -> None:
        self.logger.info('Detaching Mixxx image...', 'yellow', indentation=depth)
        self.process_adapter.run(depth, 'hdiutil', 'detach', '/Volumes/Mixxx')
        self.logger.info('Mixxx image detached.', indentation=depth)
