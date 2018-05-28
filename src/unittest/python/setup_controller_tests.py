
import unittest

from dmr.controller.setup.setup_controller import SetupController
from dmr.controller.setup.setup_behavior import SetupBehavior
from dmr.controller.setup.platform_adapter import PlatformAdapter
from dmr.controller.setup import SetupControllerModule

from mockito import mock, verify, when


class SetupControllerTest(unittest.TestCase):

    def setUp(self):
        self.mock_platform_adapter: PlatformAdapter = mock()
        self.setup_controller: SetupController = SetupController(platform_adapter=self.mock_platform_adapter)

    def test_setup_controller_calls_setup_behavior(self):
        mock_setup_behavior: SetupBehavior = mock()

        when(mock_setup_behavior).get_system_name().thenReturn('mock_system')
        when(self.mock_platform_adapter).get_system().thenReturn('mock_system')

        self.setup_controller.add_setup_behavior(mock_setup_behavior)

        self.setup_controller.do_setup()

        verify(mock_setup_behavior).do_setup()

    def test_undefined_behavior_exception(self):
        when(self.mock_platform_adapter).get_system().thenReturn('mock_system')
        self.assertRaises(Exception, self.setup_controller.do_setup)
