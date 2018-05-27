
from typing import List
from .setup_step import ISetupStep


class SetupBehavior(object):

    def __init__(self, **kwargs):
        self.setup_steps: List[ISetupStep] = []

    def add_setup_step(self, setup_step: ISetupStep) -> None:
        self.setup_steps.append(setup_step)

    def do_setup(self) -> None:
        for step in self.setup_steps:
            step.execute()

    def get_system_name(self) -> str:
        raise NotImplementedError()
