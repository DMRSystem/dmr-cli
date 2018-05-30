
from dmr.controller.setup.setup_step import ISetupStep, AbstractSetupStepDecorator
from dmr.utils.logging.logging_adapter import ILoggingAdapter

from dmr.utils.process.process_adapter import ProcessAdapter

from pathlib import Path


class MixxxInstaller(ISetupStep):

    def __init__(self, logging_adapter: ILoggingAdapter, process_adapter: ProcessAdapter):
        self.logger: ILoggingAdapter = logging_adapter
        self.process_adapter: ProcessAdapter = process_adapter

    def execute(self) -> None:
        self.logger.info('Installing Mixxx...', 'yellow')
        self.logger.info('Copying Mixxx.app to /Applications...', indentation=1)
        self.process_adapter.run('cp', '-a', '/Volumes/Mixxx/Mixxx.app', '/Applications')
        self.logger.info('Mixxx.app copied.', indentation=1)
        self.logger.info('Mixxx installed.', indentation=1)

