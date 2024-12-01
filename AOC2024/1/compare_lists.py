class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.a = []
        self.b = []

    def parse(self):
        with open(self.filename) as f:
            for line in f:
                line = line.strip()
                line = line.split()
                self.a.append(int(line[0]))
                self.b.append(int(line[1]))
        
        return self.a, self.b
    

class CompareAndAddDifferences:
    def __init__(self, a, b):
        self.difference = 0 
        self.similarity_score = 0
        self.a = a
        self.b = b
        self.input_length = len(self.a)
        self.sort()

    def sort(self):
        self.a.sort(reverse=True)
        self.b.sort(reverse=True)

    
    def compare_and_add_differences(self):
        for index,number in enumerate(self.a):
            result = abs(number - self.b[index])
            self.difference += result
        
        return self.difference

    def calculate_similarity_score(self):
        for index, number in enumerate(self.a):
            copy_b = self.b.copy()
            while len(copy_b) > 0:
                try:
                    copy_b.remove(number)
                except ValueError:
                    break

            self.similarity_score += number*(self.input_length - len(copy_b))
        
        return self.similarity_score

    
if __name__ == "__main__":
    p = Parser("input.txt")
    a, b = p.parse()
    c = CompareAndAddDifferences(a, b)
    print(f"Total distance between lists is: {c.compare_and_add_differences()}")
    print(f"Similarity score of two lists is: {c.calculate_similarity_score()}")
