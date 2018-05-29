
class ISetupStep(object):

    def execute(self) -> None:
        raise NotImplementedError()


class AbstractSetupStepDecorator(ISetupStep):

    def __init__(self, underlying_setup_step: ISetupStep):
        self._underlying_setup_step = underlying_setup_step

    def execute(self):
        self._underlying_setup_step.execute()
