
from dmr.controller.setup.setup_step import ISetupStep
from dmr.utils.logging.logging_adapter import ILoggingAdapter


class MixxxDownloadMounter(ISetupStep):

    def __init__(self, logging_adapter):
        self.logger: ILoggingAdapter = logging_adapter

    def execute(self) -> None:
        self.logger.info('Mounting Mixxx image...', 'yellow')
        # TODO: Actually mount the image
        self.logger.info('Mixxx image mounted.')
