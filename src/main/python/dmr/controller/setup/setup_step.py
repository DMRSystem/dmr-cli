
from typing import List


class ISetupStep(object):

    def execute(self, depth: int = 0) -> None:
        raise NotImplementedError()


class CompositeSetupStep(ISetupStep):

    def __init__(self):
        self._setup_steps: List[ISetupStep] = []

    def add_setup_step(self, setup_step: ISetupStep):
        self._setup_steps.append(setup_step)

    def before_execute(self, depth: int):
        pass

    def execute(self, depth: int = 0) -> None:
        self.before_execute(depth)
        for step in self._setup_steps:
            step.execute(depth+1)
        self.after_execute(depth)

    def after_execute(self, depth: int):
        pass


class AbstractSetupStepDecorator(ISetupStep):

    def __init__(self, underlying_setup_step: ISetupStep):
        self._underlying_setup_step = underlying_setup_step

    def execute(self, depth: int = 0) -> None:
        self._underlying_setup_step.execute(depth)
