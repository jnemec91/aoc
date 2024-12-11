import time

class Parser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        with open(self.file_name, 'r') as file:
            data = file.read()
            return data.split(' ')

def calculate_stone(stone, cache):
    if stone in cache:
        return cache[stone]
    
    if len(stone) % 2 == 0 and len(stone) > 1:
        first_half = stone[:len(stone) // 2]
        second_half = stone[len(stone) // 2:]
        result = [str(int(first_half)), str(int(second_half))]
    else:
        result = [str(int(stone) * 2024)]
    
    cache[stone] = result
    return result

if __name__ == '__main__':
    parser = Parser('input.txt')
    stones = parser.parse()
    start = time.time()


    cache = {'0': ['1']}

    stone_counts = {}
    for stone in stones:
        stone_counts[stone] = stone_counts.get(stone, 0) + 1

    for iteration in range(75):
        new_stone_counts = {}
        for stone, count in stone_counts.items():
            results = calculate_stone(stone, cache)

            for new_stone in results:
                new_stone_counts[new_stone] = new_stone_counts.get(new_stone, 0) + count

        stone_counts = new_stone_counts


    total_stones = sum(stone_counts.values())
    print(f'Total distinct stones: {len(cache)}')
    print(f'Total stones at the end of all iterations: {total_stones}')
    print(f'Total time: {time.time() - start:.4f} seconds')
