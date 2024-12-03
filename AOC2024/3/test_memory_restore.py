import unittest
import memory_restore

class TestMemoryRestore(unittest.TestCase):
    def setUp(self):
        self.restorer = memory_restore.MemoryRestorer()
        self.restorer.load_data('test_input.txt')
    
    def test_restore(self):
        self.assertEqual(self.restorer.restore(), 161)
    
    def test_restore_with_additional_instructions(self):
        self.restorer.load_data('test_input_with_additional_instructions.txt')
        self.assertEqual(self.restorer.restore_with_additional_instructions(), 48)


if __name__ == '__main__':
    unittest.main()