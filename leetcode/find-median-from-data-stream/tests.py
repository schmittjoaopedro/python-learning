import unittest

from solution import MedianFinder


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        finder = MedianFinder()
        finder.addNum(1)
        finder.addNum(2)
        self.assertEqual(1.5, finder.findMedian())
        finder.addNum(3)
        self.assertEqual(2, finder.findMedian())

    def test_case2(self):
        finder = MedianFinder()
        finder.addNum(-1)
        self.assertEqual(-1, finder.findMedian())
        finder.addNum(-2)
        self.assertEqual(-1.5, finder.findMedian())
        finder.addNum(-3)
        self.assertEqual(-2, finder.findMedian())
        finder.addNum(-4)
        self.assertEqual(-2.5, finder.findMedian())
        finder.addNum(-5)
        self.assertEqual(-3, finder.findMedian())

    def test_case3(self):
        finder = MedianFinder()
        finder.addNum(6)
        self.assertEqual(6, finder.findMedian())
        finder.addNum(10)
        self.assertEqual(8, finder.findMedian())
        finder.addNum(2)
        self.assertEqual(6, finder.findMedian())
        finder.addNum(6)
        self.assertEqual(6, finder.findMedian())
        finder.addNum(5)
        self.assertEqual(6, finder.findMedian())
        finder.addNum(0)
        self.assertEqual(5.5, finder.findMedian())
        finder.addNum(6)
        self.assertEqual(6, finder.findMedian())
        finder.addNum(3)
        self.assertEqual(5.5, finder.findMedian())
        finder.addNum(1)
        self.assertEqual(5, finder.findMedian())
        finder.addNum(0)
        self.assertEqual(4, finder.findMedian())
        finder.addNum(0)
        self.assertEqual(3, finder.findMedian())
