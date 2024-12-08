
import math

class Parser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        with open(self.file_name) as f:
            return [[i for i in line.strip()] for line in f]


def get_antena_types(antenna_map):
    antena_types = set()
    for line in antenna_map:
        for antena in line:
            if antena not in '#.':
                antena_types.add(antena)
    return antena_types

def get_antena_positions(antena_type, antena_map):
    positions = []
    for i in range(len(antena_map)):
        for j in range(len(antena_map[i])):
            if antena_map[i][j] == antena_type:
                positions.append((i, j))
    return positions


def find_antinodes(antenna_map):
    antena_types = get_antena_types(antenna_map)
    antinodes = set()

    for type in antena_types:
        positions = get_antena_positions(type, antenna_map)
        for position in positions:
            for position2 in positions:
                if position != position2:
                    distance_x = position[0] - position2[0]
                    distance_y = position[1] - position2[1]

                    antinodes.add(
                        (position[0] + distance_x, position[1] + distance_y)
                    )
                    # for part two add also all the points in line with the two antenas
                    for i in range(0, len(antenna_map)):
                        for j in range(0, len(antenna_map[i])):
                            if (i - position[0]) * (position2[1] - position[1]) == (j - position[1]) * (position2[0] - position[0]):
                                antinodes.add((i, j))
    to_remove = []
    for antinode in antinodes:
        if antinode[0] < len(antenna_map) and antinode[1] < len(antenna_map[0]) and antinode[0] >= 0 and antinode[1] >= 0:
            antenna_map[antinode[0]][antinode[1]] = '#' if antenna_map[antinode[0]][antinode[1]] == '.' else 'X'
        else:
            to_remove.append(antinode)
            
    for remove in to_remove:
        antinodes.remove(remove)
    
    for line in antenna_map:
        print(''.join(line))
    
    return len([i for i in antinodes])


antenna_map = Parser("input.txt").parse()
print(find_antinodes(antenna_map))