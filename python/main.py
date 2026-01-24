from src.xunit import TestCaseTest

if __name__ == "__main__":
    print(TestCaseTest("testTemplateMethod").run().summary())
    print(TestCaseTest("testResult").run().summary())
    print(TestCaseTest("testFailedResultFormatting").run().summary())
    print(TestCaseTest("testFailedResult").run().summary())
