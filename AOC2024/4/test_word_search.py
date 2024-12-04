import unittest
import word_search

class TestEightDirectionSearch(unittest.TestCase):

    def setUp(self):
        self.parser = word_search.Parser("test_input.txt")
        self.grid = self.parser.parse()
        self.searcher = word_search.WordSearcher(self.grid)
    
    def test_search_for_starting_letter(self):
        self.assertEqual(len(self.searcher._search_for_starting_letter('X')), 12)
        self.assertIsInstance(self.searcher._search_for_starting_letter('X'), list)
    
    def test_search_eight_directions(self):
        self.searcher._search_eight_directions("XMAS", 0, 5)
        self.assertEqual(self.searcher.number_of_occurrences, 1)

    def test_search(self):
        self.assertEqual(self.searcher.search_word("XMAS"), 18)


class TestXShapeSearch(unittest.TestCase):
        def setUp(self):
            self.parser = word_search.Parser("test_input_mas_in_shape.txt")
            self.grid = self.parser.parse()
            self.searcher = word_search.WordSearcher(self.grid)
        
        def test_search_for_x_shape(self):               
            self.assertEqual(self.searcher._search_for_x_shape("MAS", 1, 2), 1)
            self.assertEqual(self.searcher._search_for_x_shape("MAS", 1, 5), 0)
                 
        def test_search_x_shape_words(self):
            self.assertEqual(self.searcher.search_x_shape_words("MAS"), 9)


if __name__ == "__main__":
    unittest.main()