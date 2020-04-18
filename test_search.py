import unittest

import search


class TestSearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(search.binary_search([24, 10, 1, 64, 99, 9, 12], 9), 1)
        self.assertEqual(search.binary_search([20, 10, 31, 4, 800, 799, 600], 600), 4)
        self.assertEqual(search.binary_search([4, 10, 21, 16, 19, 27, 5, 7], 7), 2)

    def test_binary_search1(self):
        self.assertEqual(search.binary_search([10, 100, 800, 1, 35, 17], 11), None)
        self.assertEqual(search.binary_search([-4, 10, 2, 20, 100, 800, 1, 35, 17], 1000), None)
        self.assertEqual(search.binary_search([4, -40, 2, 20, 600, 60, 1, 35, 17], 150), None)
