class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()


class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp"

    def testMethod(self):
        self.log = self.log + " testMethod"

    def testBrokenMethod(self):
        raise Exception

    def tearDown(self):
        self.log = self.log + " tearDown"


class SetUpFailed(TestCase):
    def setUp(self):
        raise Exception

    def testMethod(self):
        pass


class TestResult:
    def __init__(self):
        self.runcount = 0
        self.errorcount = 0

    def testStarted(self):
        self.runcount += 1

    def testFailed(self):
        self.errorcount += 1

    def summary(self):
        return f"{self.runcount} run, {self.errorcount} failed"


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert test.log == "setUp testMethod tearDown"

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 0 failed"

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert self.result.summary() == "1 run, 1 failed"

    def testSetUpFailedResult(self):
        test = SetUpFailed("testMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert result.summary() == "2 run, 1 failed"


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testSuite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
