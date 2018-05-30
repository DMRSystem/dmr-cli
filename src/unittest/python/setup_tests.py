
from dmr.cli.command.setup import setup

import unittest


class SetupTest(unittest.TestCase):

    @unittest.skip('debugging purposes')
    def test_setup(self):
        setup()
