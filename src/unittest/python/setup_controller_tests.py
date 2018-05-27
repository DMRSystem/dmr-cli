
import unittest

from dmr.controller.setup.setup_controller import SetupController
from dmr.controller.setup.setup_step import ISetupStep

from mockito import mock, verify


class SetupControllerTest(unittest.TestCase):

    def setUp(self):
        self.setup_controller: SetupController = SetupController()

    def test_setup_controller_calls_setup_step(self):
        mock_setup_step: ISetupStep = mock()

        self.setup_controller.add_setup_step(mock_setup_step)

        self.setup_controller.do_setup()

        verify(mock_setup_step).execute()
