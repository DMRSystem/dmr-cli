
import unittest
from dmr.controller.setup.setup_behavior import SetupBehavior
from dmr.controller.setup.setup_step import ISetupStep

from mockito import mock, verify

class SetupBehaviorTest(unittest.TestCase):

    def setUp(self):
        self.mock_system_name: str = 'mock_system_name'
        self.setup_behavior: SetupBehavior = SetupBehavior(self.mock_system_name)

    def test_get_system_name(self):
        self.assertEqual(self.mock_system_name, self.setup_behavior.get_system_name())

    def test_add_single_setup_step(self):
        mock_setup_step: ISetupStep = mock()

        self.setup_behavior.add_setup_step(mock_setup_step)

        self.setup_behavior.do_setup()

        verify(mock_setup_step, times=1).execute()
