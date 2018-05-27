
import unittest
import requests

class RequestsTest(unittest.TestCase):

    @unittest.skip
    def test_download_file(self):
        response = requests.get('https://downloads.mixxx.org/mixxx-2.1.0/mixxx-2.1.0-osxintel.dmg')