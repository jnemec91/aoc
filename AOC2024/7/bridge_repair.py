import re
import os
from itertools import product

class Parser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        with open(self.filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            data = []
            for line in lines:
                result = line[:line.index(':')]
                numbers = line[line.index(':')+1:].strip().split(' ')
                data.append((result, numbers))

            return data
            

class BridgeRepair:
    def __init__(self, data):
        self.data = data
        self.sum_of_valid_equations = 0

    def repair(self, part_two=False):
        for line in self.data:
            os.system('cls')
            print(f'Processing line {self.data.index(line)+1}/{len(self.data)}')
            result = int(line[0])
            numbers = line[1]
            all_possible_strings = self._get_all_possible_strings(numbers, part_two=part_two)
            all_possible_strings = [self._evaluate(x) for x in all_possible_strings]

            if any(x == result for x in all_possible_strings):
                self.sum_of_valid_equations += int(result)

        return self.sum_of_valid_equations

    def _get_all_possible_strings(self, numbers, part_two=False):
        if part_two:
            operators = ['+', '*', '||']
        else:
            operators = ['+', '*']

        all_possible_strings = []

        for ops in product(operators, repeat=len(numbers)-1):
            string = numbers[0]
            for num, op in zip(numbers[1:], ops):
                string += op + num
            all_possible_strings.append(string)

        return all_possible_strings

    def _evaluate(self, string):
        tokens = re.split(r'(\+|\*|\|\|)', string)
        result = int(tokens[0])
        i = 1
        while i < len(tokens):
            operator = tokens[i]
            next_number = int(tokens[i + 1])
            if operator == '+':
                result += next_number
            elif operator == '*':
                result *= next_number
            elif operator == '||':
                result = int(str(result) + str(next_number))
            i += 2

        return result
    

if __name__ == '__main__':
    p = Parser('input.txt')
    d = p.parse()

    b1= BridgeRepair(d)
    part_one = b1.repair()
    b2 = BridgeRepair(d)
    part_two = b2.repair(part_two=True)
    
    print(f'Sum of all possible operations is {part_one}')
    print(f'Sum of all possible operations with additional operator is {part_two}')