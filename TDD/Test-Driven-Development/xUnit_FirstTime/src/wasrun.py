from test_case import TestCase


class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp"

    def testMethod(self):
        self.wasRun = 1
