

from dmr.controller.setup.setup_step import ISetupStep
import unittest


class SetupStepTest(unittest.TestCase):

    def setUp(self):
        self.setup_step: ISetupStep = ISetupStep()

    def test_not_implemented_exception(self):
        self.assertRaises(NotImplementedError, self.setup_step.execute)
