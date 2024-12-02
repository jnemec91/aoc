import compare_lists
import unittest

class TestCompareLists(unittest.TestCase):  
    def setUp(self):
        p = compare_lists.Parser("test_input.txt")
        a, b = p.parse()
        self.c = compare_lists.CompareAndAddDifferences(a, b)

    def test_compare_and_add_differences(self):
        self.assertEqual(self.c.compare_and_add_differences(), 11)

    def test_calculate_similarity_score(self):
        self.assertEqual(self.c.calculate_similarity_score(), 31)
    
if __name__ == '__main__':
    unittest.main()