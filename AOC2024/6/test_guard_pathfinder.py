import unittest
import guard_pathfinder

class TestGuardPathfinder(unittest.TestCase):
    def setUp(self):
        self.parser = guard_pathfinder.Parser('test_input.txt')
        self.maze = self.parser.parse()
        self.guard = guard_pathfinder.find_guard(self.maze)

    def test_find_guard(self):
        self.assertEqual(self.guard, (6, 4))
    
    def test_check_direction(self):
        self.assertEqual(guard_pathfinder.check_direction(self.guard, '^'), (5, 4))
        self.assertEqual(guard_pathfinder.check_direction(self.guard, 'v'), (7, 4))
        self.assertEqual(guard_pathfinder.check_direction(self.guard, '<'), (6, 3))
        self.assertEqual(guard_pathfinder.check_direction(self.guard, '>'), (6, 5))
    
    def test_check_maze(self):
        self.assertEqual(len(guard_pathfinder.check_maze(self.maze, self.guard)), 41)

if __name__ == '__main__':
    unittest.main()