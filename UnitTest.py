from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ([3,4,5,1,2], True), 2: ([2,1,3,4], False), 3: ([1,2,3], True)}
        self.__sol = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        nums, output = self.__testcases[1]
        result = self.__sol.check(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        nums, output = self.__testcases[2]
        result = self.__sol.check(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_3(self):
        nums, output = self.__testcases[3]
        result = self.__sol.check(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()