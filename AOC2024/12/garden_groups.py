class Parser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        with open(self.file_name) as f:
            return [[i for i in line.strip()] for line in f]

class Plant:
    def __init__(self, plant_type, x, y, row_lenght, column_lenght):
        self.plant_type = plant_type
        self.x = x
        self.y = y
        self.neighbors = []
        self.already_part_of_group = False
        self.exposed_sides = 0

        if self.x == 0 or self.x == row_lenght - 1:
            self.exposed_sides += 1
        if self.y == 0 or self.y == column_lenght - 1:
            self.exposed_sides += 1


    def __repr__(self):
        return f'{self.plant_type}({self.x}, {self.y})'
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y and self.plant_type == value.plant_type
    
    def __hash__(self):
        return hash((self.x, self.y, self.plant_type))
    
    def find_neighbors(self, garden):
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = self.x + direction[0], self.y + direction[1]
            if x < 0 or x >= len(garden) or y < 0 or y >= len(garden[0]):
                continue
            self.neighbors.append(garden[x][y])

            if direction == (0, 1):
                self.left = garden[x][y]
            elif direction == (0, -1):
                self.right = garden[x][y]
            elif direction == (1, 0):
                self.bottom = garden[x][y]
            elif direction == (-1, 0):
                self.top = garden[x][y]


def find_groups_of_same_plants(plant, group=[]):
    if plant.already_part_of_group:
        return group
    plant.already_part_of_group = True
    group.append(plant)
    for neighbor in plant.neighbors:
        if neighbor.plant_type == plant.plant_type:
            find_groups_of_same_plants(neighbor, group)
        else:
            plant.exposed_sides += 1
    
    return group


def calculate_group_area(group):
    return (len(group))


def calculate_group_perimeter(group):
    return sum([plant.exposed_sides for plant in group])    
        

def calculate_group_score(group):
    return calculate_group_area(group) * calculate_group_perimeter(group)


def calculate_number_of_corners(group):
    corners = 0
    if len(group) == 1:
        return 4
     
    for plant in group:
        if plant.exposed_sides == 3:
            corners += 2

        elif plant.exposed_sides == 2:
            left_right = []
            for direction in [(0, 1), (0, -1)]:
                x, y = plant.x + direction[0], plant.y + direction[1]
                if x < 0 or x >= len(garden) or y < 0 or y >= len(garden[0]):
                    left_right += [(None,None)]
                    continue
                if garden[x][y].plant_type != plant.plant_type:
                    left_right += [(x, y)]
                    
            top_bottom = []
            for direction in [(1, 0), (-1, 0)]:
                x, y = plant.x + direction[0], plant.y + direction[1]
                if x < 0 or x >= len(garden) or y < 0 or y >= len(garden[0]):
                    top_bottom += [(None,None)]
                    continue
                if garden[x][y].plant_type != plant.plant_type:
                    top_bottom += [(x, y)]

            if len(left_right) == 2 or len(top_bottom) == 2:
                continue

            else:
                corners += 1


    print(group, corners)
    return corners

def calculate_bulk_cost(group):
    return calculate_group_area(group) * calculate_number_of_corners(group)


if __name__ == '__main__':
    parser = Parser('test_input.txt')
    garden = parser.parse()
    garden = [[Plant(plant, cr, cp, len(garden[0]), len(garden)) for cp, plant in enumerate(row)] for cr, row in enumerate(garden)]

    plants = []
    for row in garden:
        for plant in row:
            plant.find_neighbors(garden)
            plants.append(plant)

    plant_groups = []

    total_cost = 0
    total_sides = 0

    for plant in plants:
        if plant.already_part_of_group:
            continue
        group = find_groups_of_same_plants(plant, [])
        if group:
            plant_groups.append(group)

            total_cost += calculate_group_score(group)
            total_sides += calculate_bulk_cost(group)

    print(f'Total cost of fence is {total_cost}')
    print(f'Total cost of fence when buing in bulk is {total_sides}')