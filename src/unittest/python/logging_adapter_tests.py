
import unittest
from dmr.utils.logging.logging_adapter import ILoggingAdapter


class ILoggingAdapterTest(unittest.TestCase):

    def setUp(self):
        self.logging_adapter: ILoggingAdapter = ILoggingAdapter()

    def test_not_implemented_exception(self):
        self.assertRaises(NotImplementedError, self.logging_adapter.info, '')
