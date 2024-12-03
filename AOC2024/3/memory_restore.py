import re

class MemoryRestorer:
    def __init__(self):
        self.memory = ''
        self.result = 0
        self.result_with_more_instructions = 0

    def load_data(self, data_file):
        with open(data_file) as file:
            self.memory = file.read()
        
    def restore(self):
        pattern = r'(mul\(\d+\,\d+\))'
        for i in re.findall(pattern, self.memory):
            operands = re.findall(r'\d+', i)
            self.result += int(operands[0]) * int(operands[1])
        
        return self.result

    def restore_with_additional_instructions(self):
        do_pattern = r'(do\(\))'
        dont_pattern = r'(don\'t\(\))'
        mul_pattern = r'(mul\(\d+\,\d+\))'
    
        add = True

        while True:
            search_result = {'search_do':re.search(do_pattern, self.memory),
            'search_dont':re.search(dont_pattern, self.memory),
            'search_mul':re.search(mul_pattern, self.memory),}
            compare = [result for key, result in search_result.items() if result is not None]

            if len(compare) == 0:
                break

            first_occurrence = min(compare, key=lambda x: x.start())

            if first_occurrence is None:
                break
                
            if first_occurrence == search_result['search_do']:
                add = True
                self.memory = self.memory[first_occurrence.end()::]
            
            elif first_occurrence == search_result['search_dont']:
                add = False
                self.memory = self.memory[first_occurrence.end()::]
            
            elif first_occurrence == search_result['search_mul']:
                operands = re.findall(r'\d+', first_occurrence.group())
                if add:
                    self.result_with_more_instructions += int(operands[0]) * int(operands[1])

                self.memory = self.memory[first_occurrence.end()::]

        return self.result_with_more_instructions
        

if __name__ == '__main__':
    restorer = MemoryRestorer()
    restorer.load_data('input.txt')
    print(f'Result of restored program is: {restorer.restore()}')
    print(f'Result of restored program with additional instructions is: {restorer.restore_with_additional_instructions()}')