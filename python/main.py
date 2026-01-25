from src.xunit import TestCaseTest, TestResult, TestSuite

if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSuite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
