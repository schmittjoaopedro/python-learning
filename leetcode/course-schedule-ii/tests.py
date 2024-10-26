import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]
        self.assertEqual(expected, Solution().findOrder(numCourses, prerequisites))

    def test_case2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [0, 1, 2, 3]
        self.assertEqual(expected, Solution().findOrder(numCourses, prerequisites))

    def test_case3(self):
        numCourses = 1
        prerequisites = []
        expected = [0]
        self.assertEqual(expected, Solution().findOrder(numCourses, prerequisites))

    def test_case4(self):
        numCourses = 2
        prerequisites = [[0, 1], [1, 0]]
        expected = []
        self.assertEqual(expected, Solution().findOrder(numCourses, prerequisites))

    def test_case5(self):
        numCourses = 3
        prerequisites = [[0, 1], [0, 2], [1, 2]]
        expected = [2, 1, 0]
        self.assertEqual(expected, Solution().findOrder(numCourses, prerequisites))
