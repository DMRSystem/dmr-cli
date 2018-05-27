
from .setup_step import ISetupStep
from typing import List


class SetupController(object):

    def __init__(self):
        self.setup_steps: List = []

    def add_setup_step(self, setup_step: ISetupStep) -> None:
        self.setup_steps.append(setup_step)

    def do_setup(self) -> None:
        pass