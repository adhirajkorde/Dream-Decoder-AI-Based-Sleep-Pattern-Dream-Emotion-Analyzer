import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.test_accuracy import TestDreamAccuracy

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDreamAccuracy)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*50)
    print(f"Test Summary:")
    print(f"Total Tests: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*50)
    
    if result.failures:
        print("\nFAILURES:")
        for test, err in result.failures:
            print(f"- {test._testMethodName}: {err}")
            
    if result.errors:
        print("\nERRORS:")
        for test, err in result.errors:
            print(f"- {test._testMethodName}: {err}")

if __name__ == "__main__":
    run_tests()
