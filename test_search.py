import unittest

import search


class TestSearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(search.binary_search([4, 10, 2, 20, 100, 800, 1, 35, 17], 11), None)
        self.assertEqual(search.binary_search([24, 10, 1, 64, 99, 9, 12], 9), 1)
        self.assertEqual(search.binary_search([20, 10, 31, 4, 800, 799, 600], 600), 4)

