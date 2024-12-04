class Parser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        with open(self.file) as f:
            lines = f.read()
            grid = [[i for i in line] for line in lines.splitlines()]
            return grid

class WordSearcher:
    def __init__(self, grid):
        self.grid = grid
        self.number_of_occurrences = 0
        self.number_of_shapes = 0
        self.debug_coordinates = []


    def _search_for_starting_letter(self, letter):
        positions = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == letter:
                    positions.append((i, j))

        return positions


    def _search_eight_directions(self, word, x, y):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
        for direction in directions:
            dx, dy = direction
            for i in range(len(word)):
                new_x = x + i * dx
                new_y = y + i * dy
                if new_x < 0 or new_x >= len(self.grid) or new_y < 0 or new_y >= len(self.grid[0]):
                    break
                if self.grid[new_x][new_y] != word[i]:
                    break
            else:
                self.number_of_occurrences += 1
                self.debug_coordinates.append((x, y))


    def search_word(self, word):
        starting_letters = self._search_for_starting_letter(word[0])
        for x, y in starting_letters:
            self._search_eight_directions(word, x, y)

        return self.number_of_occurrences
            

    def _search_for_x_shape(self, word, x,y):
        found_words = []

        poissible_combinations = [[(1, 1),(0, 0),(-1, -1)],[(-1, -1),(0, 0),(1, 1)], [(1, -1), (0,0), (-1, 1)], [(-1, 1), (0,0), (1, -1)]]
        for combination in poissible_combinations:
            found_word = ''
            for letter in combination:
                dx, dy = letter
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= len(self.grid) or new_y < 0 or new_y >= len(self.grid[0]):
                    break
                found_word += self.grid[new_x][new_y]

            if found_word == word:
                found_words.append(found_word)

        if len(found_words) == 2:
            return 1
    
        return 0

    def search_x_shape_words(self, word):
        starting_letters = self._search_for_starting_letter(word[1])
        for x, y in starting_letters:
            self.number_of_shapes += self._search_for_x_shape(word, x, y)

        return self.number_of_shapes



if __name__ == "__main__":
    parser = Parser("input.txt")
    grid = parser.parse()
    searcher = WordSearcher(grid)
    print(f'Number of XMAS in grid is {searcher.search_word("XMAS")}.')
    print(f'Number of MAS in shape of X in grid is {searcher.search_x_shape_words("MAS")}.')