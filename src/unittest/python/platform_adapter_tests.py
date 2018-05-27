

import unittest

import platform

from dmr.controller.setup.platform_adapter import PlatformAdapter


class PlatformAdapterTest(unittest.TestCase):

    def setUp(self):
        self.platform_adapter: PlatformAdapter = PlatformAdapter()

    def test_get_system(self):
        expected: str = platform.system()
        actual: str = self.platform_adapter.get_system()
        self.assertEqual(expected, actual)

