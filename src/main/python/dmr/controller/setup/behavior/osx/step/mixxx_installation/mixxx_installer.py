
from dmr.controller.setup.setup_step import CompositeSetupStep
from dmr.controller.setup.setup_step import AbstractSetupStepDecorator
from dmr.controller.setup.setup_step import ISetupStep
from dmr.utils.logging.logging_adapter import ILoggingAdapter
import sys
from pathlib import Path


class MixxxInstaller(CompositeSetupStep):

    def __init__(self, logging_adapter: ILoggingAdapter):
        CompositeSetupStep.__init__(self)
        self.logger: ILoggingAdapter = logging_adapter

    def before_execute(self, depth: int):
        self.logger.info('Installing Mixxx...', color='yellow', indentation=depth)

    def after_execute(self, depth: int):
        self.logger.info('Mixxx installed.', color='yellow', indentation=depth)


class AlreadyInstalledCheckDecorator(AbstractSetupStepDecorator):

    def __init__(self, setup_step: ISetupStep, logging_adapter: ILoggingAdapter):
        AbstractSetupStepDecorator.__init__(self, setup_step)
        self.logger = logging_adapter

    def execute(self, depth: int = 0):
        if self._mixxx_already_installed():
            self.logger.info('Mixxx already installed at /Applications/Mixxx.app', 'blue', depth)
            self.logger.info('Skipping installation.', indentation=depth)
            sys.exit(0)
        AbstractSetupStepDecorator.execute(self)

    def _mixxx_already_installed(self):
        return Path('/', 'Applications', 'Mixxx.app').exists()