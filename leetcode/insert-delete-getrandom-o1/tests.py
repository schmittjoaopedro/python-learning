import unittest

from solution import RandomizedSet


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        obj = RandomizedSet()
        self.assertTrue(obj.insert(1))
        self.assertFalse(obj.remove(2))
        self.assertTrue(obj.insert(2))
        self.assertIn(obj.getRandom(), [1, 2])
        self.assertTrue(obj.remove(1))
        self.assertFalse(obj.insert(2))
        self.assertEqual(obj.getRandom(), 2)
