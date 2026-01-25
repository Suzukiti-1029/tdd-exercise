from typing import List, override


class TestResult:
    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return f"{self.runCount} run, {self.errorCount} failed"


class TestCase:
    def __init__(self, name: str):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result: TestResult) -> None:
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()


class TestSuite:
    def __init__(self) -> None:
        self.tests: List[TestCase] = []

    def add(self, test: TestCase) -> None:
        self.tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self.tests:
            test.run(result)


class WasRun(TestCase):
    @override
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        raise Exception

    @override
    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testFailedResultFormatting(self):
        """
        testFailedResultFormatting は TestResult の単体テスト
        """
        self.result.testStarted()
        self.result.testFailed()
        assert "1 run, 1 failed" == self.result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()
