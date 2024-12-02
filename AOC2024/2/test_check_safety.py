import check_safety
import unittest

class TestCheckSafety(unittest.TestCase):
    def setUp(self):
        p = check_safety.Parser("test_input.txt")
        reports = p.parse()
        self.s = check_safety.SafetyChecker(reports)

    def test_check_safety(self):
        self.assertEqual(self.s.check_safety(self.s.reports), 2)
    
    def test_construct_list_with_skipped_value(self):
        self.assertEqual(self.s._construct_list_with_skipped_value([1, 2, 3], 1), [1, 3])
    
    def test_construct_all_possible_lists(self):
        self.assertEqual(self.s._construct_all_possible_lists([[1, 2, 3], [4, 5, 6]]), [[[2, 3], [1, 3], [1, 2]], [[5, 6], [4, 6], [4, 5]]])
                        
    def test_check_safety_with_problem_dampener(self):
        self.assertEqual(self.s.check_safety_with_problem_dampener(self.s.reports), 4)
    

if __name__ == '__main__':
    unittest.main()