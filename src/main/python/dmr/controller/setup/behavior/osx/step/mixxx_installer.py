
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


class AlreadyInstalledCheckDecorator(AbstractSetupStepDecorator):

    def __init__(self, setup_step: ISetupStep, logging_adapter: ILoggingAdapter):
        AbstractSetupStepDecorator.__init__(self, setup_step)
        self.logger = logging_adapter

    def execute(self):
        if self._mixxx_already_installed():
            self.logger.info('Mixxx already installed at /Applications/Mixxx.app', 'blue')
            self.logger.info('Skipping installation.', indentation=1)
            return
        AbstractSetupStepDecorator.execute(self)

    def _mixxx_already_installed(self):
        return Path('/', 'Applications', 'Mixxx.app').exists()
