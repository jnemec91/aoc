
class Parser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        with open(self.file_name) as f:
            compressed_data = f.read().strip()

            # initial setup
            data, files, spaces = [], [], []
            writing_data = True
            data_id = 0

        for block_length in map(int, compressed_data):
            if writing_data:
                files.append((len(data), block_length))
                for l in range(block_length):
                    data.append(data_id)
                data_id += 1
                writing_data = False
            else:
                spaces.append((len(data), block_length))
                for l in range(block_length):
                    data.append(".")
                writing_data = True
            
        return data, files, spaces        


def checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if isinstance(disk[i], str):
            continue
        checksum += disk[i]*i
    
    return checksum


def sort_data(disk):
    write_head = 0
    read_head = len(disk) - 1

    while write_head < read_head:
        while isinstance(disk[read_head], str):
            read_head -= 1
        while isinstance(disk[write_head], int):
            write_head += 1

        if write_head >= read_head:
            break
        data = disk[read_head]
        space = disk[write_head]
        disk[write_head] = data
        disk[read_head] = space
    
    return disk


def sort_files(disk, files, spaces):
    for file_start, file_length in reversed(files):
        for space_start, space_length in spaces:
            if space_start > file_start:
                break

            if space_length >= file_length:
                disk[space_start : space_start + file_length] = disk[file_start : file_start + file_length]
                disk[file_start : file_start + file_length] = ["."] * file_length

                index = spaces.index((space_start, space_length))

                if file_length < space_length:
                    spaces[index] = (space_start + file_length, space_length - file_length)
                else:
                    spaces.pop(index)
                break

    return disk

    
if __name__ == '__main__':
    parser = Parser('input.txt')
    disk, files, spaces = parser.parse()
    print(f'Checksum for part one is: {checksum(sort_data(disk))}')

    disk, files, spaces = parser.parse()
    print(f'Checksum for part two is: {checksum(sort_files(disk, files, spaces))}')
