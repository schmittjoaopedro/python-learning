import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3]
        Solution().nextPermutation(nums)
        self.assertEqual([1, 3, 2], nums)
        Solution().nextPermutation(nums)
        self.assertEqual([2, 1, 3], nums)
        Solution().nextPermutation(nums)
        self.assertEqual([2, 3, 1], nums)
        Solution().nextPermutation(nums)
        self.assertEqual([3, 1, 2], nums)
        Solution().nextPermutation(nums)
        self.assertEqual([3, 2, 1], nums)
        Solution().nextPermutation(nums)
        self.assertEqual([1, 2, 3], nums)

    def test_case2(self):
        nums = [1, 2, 3, 4, 5]
        print("")
        while True:
            print(nums)
            Solution().nextPermutation(nums)
            if nums == [1, 2, 3, 4, 5]:
                break

    def test_case3(self):
        self.assertEqual("abd", Solution().nextSpecialString("abc"))
        self.assertEqual("-1", Solution().nextSpecialString("zzab"))
        self.assertEqual("abcdab", Solution().nextSpecialString("abccde"))
        self.assertEqual("abca", Solution().nextSpecialString("abbd"))
        self.assertEqual("baba", Solution().nextSpecialString("azza"))

    def test_case4(self):
        self.assertEqual([9], Solution().findNetworkCalls([4, 6, 5, 2, 1], [3]))
        self.assertEqual([10, 20], Solution().findNetworkCalls([3, 6, 2, 6, 3], [6, 8]))
        self.assertEqual([4, 3], Solution().findNetworkCalls([3, 6, 6], [5, 6]))
