class Parser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        with open(self.file_name, 'r') as file:
            return [[int(item) for item in line] for line in file.read().splitlines()]

class TrailNode:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y, self.value))

    def get_neighbors(self, trail_map):
        neighbors = []
        if self.x > 0:
            neighbors.append(trail_map[self.y][self.x - 1])
        if self.x < len(trail_map[0]) - 1:
            neighbors.append(trail_map[self.y][self.x + 1])
        if self.y > 0:
            neighbors.append(trail_map[self.y - 1][self.x])
        if self.y < len(trail_map) - 1:
            neighbors.append(trail_map[self.y + 1][self.x])
        
        return neighbors
    
    
def get_all_paths_to_nine(node, visited):
    if node not in visited:
        visited.add(node)
        if node.value == 9:
            return 1
        score = 0
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if neighbor.value == node.value+1:
                    score += get_all_paths_to_nine(neighbor, visited)
        return score
    return 0


def part_one():
    total_score = 0
    for node in nodes:
        visited = set()
        if node.value == 0:
            score = get_all_paths_to_nine(node, visited)
            total_score += score

    print(f'Total score: {total_score}')
    

def get_all_possible_paths(node):
    if node.value == 9:
        return [[node]]
    
    paths = []
    for neighbor in node.neighbors:
        if neighbor.value == node.value + 1:
            for path in get_all_possible_paths(neighbor):
                paths.append([node] + path)

    return paths


def part_two():
    total_paths = 0
    for node in nodes:
        if node.value == 0:
            paths = get_all_possible_paths(node)
            total_paths += len(paths)
    
    print(f'Total paths: {total_paths}')


if __name__ == '__main__':
    parser = Parser('input.txt')
    trail_map = parser.parse()
    nodes = []

    for x in range(len(trail_map)):
        for y in range(len(trail_map[0])):
            trail_map[x][y] = TrailNode(y, x, trail_map[x][y])
    
    for x in range(len(trail_map)):
        for y in range(len(trail_map[0])):
            trail_map[x][y].neighbors = trail_map[x][y].get_neighbors(trail_map)
            nodes.append(trail_map[x][y])

    part_one()
    part_two()