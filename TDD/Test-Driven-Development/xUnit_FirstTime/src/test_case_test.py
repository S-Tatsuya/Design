from test_case import TestCase
from wasrun import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert "setUp testMethod tearDown " == self.test.log


TestCaseTest("testTemplateMethod").run()
