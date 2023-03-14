from test_case import TestCase
from wasrun import WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        self.test.run()
        assert "setUp testMethod " == self.test.log


TestCaseTest("testTemplateMethod").run()
