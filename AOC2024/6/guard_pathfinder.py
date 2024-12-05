
    

class Parser:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def parse(self):
        with open(self.input_file, 'r') as file:
            return [[a for a in i] for i in file.read().splitlines()]

if __name__ == '__main__':
    possible_infinite_loops = 0
    parser = Parser('input.txt')
    maze = parser.parse()
    
    

    def find_guard(maze):
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == '^' or maze[i][j] == 'v' or maze[i][j] == '<' or maze[i][j] == '>':
                    return (i, j)

    guard = find_guard(maze)

    def check_direction(guard, direction):
        if direction == '^':
            return (guard[0] - 1, guard[1])
        elif direction == 'v':
            return (guard[0] + 1, guard[1])
        elif direction == '<':
            return (guard[0], guard[1] - 1)
        elif direction == '>':
            return (guard[0], guard[1] + 1)

    def check_maze(maze, guard=guard):
        visited = []
        collided_wals = []
        guard_direction = maze[guard[0]][guard[1]]
        visited.append(guard)

        while True:
            next_field = check_direction(guard, guard_direction)
            if next_field[0] < 0 or next_field[0] > len(maze)-1 or next_field[1] < 0 or next_field[1] > len(maze[0])-1:
                break
            if maze[next_field[0]][next_field[1]] == '#':
                if (next_field, guard_direction) in collided_wals:
                    return None
                collided_wals.append((next_field, guard_direction))
                if guard_direction == '^':
                    guard_direction = '>'
                elif guard_direction == '>':
                    guard_direction = 'v'
                elif guard_direction == 'v':
                    guard_direction = '<'
                elif guard_direction == '<':
                    guard_direction = '^'
            else:
                guard = next_field
                visited.append(guard)


        return list(set(visited))

    all_visited_places = check_maze(maze)
    print(len(all_visited_places))

    for place in all_visited_places:
        maze = parser.parse()
        if place == guard:
            continue
        maze[place[0]][place[1]] = '#'
        if check_maze(maze) == None:
            possible_infinite_loops += 1
    

    print(possible_infinite_loops)


