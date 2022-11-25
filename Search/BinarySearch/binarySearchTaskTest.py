import unittest

from binarySearchTask import binary_search


class TestBinarySearchTask(unittest.TestCase):
    def test_list_int(self):
        # Test 1
        result = binary_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 27)
        self.assertEqual(result.get("found"), True)
        self.assertEqual(result.get("elements_searched"), 3)
        self.assertEqual(result.get("position"), 5)

        # Test 2
        result = binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 8)
        self.assertEqual(result.get("found"), True)
        self.assertEqual(result.get("elements_searched"), 4)
        self.assertEqual(result.get("position"), 8)

        # Test 3
        result = binary_search([5, 3, 2, 5, 6], 1)
        self.assertEqual(result.get("found"), False)
        self.assertEqual(result.get("elements_searched"), 2)
        self.assertEqual(result.get("position"), 0)


if __name__ == '__main__':
    unittest.main()
