from pprint import pprint
from dataclasses import dataclass



@dataclass
class Position:
    x: int
    y: int

def check_pos(dat: list[list[Position]], x: int, y: int) -> bool:
    if x < 0 or y < 0:
        return False
    if x >= len(dat) or y >= len(dat[0]):
        return False
    return isinstance(dat[x][y], IntPos)

@dataclass
class IntPos(Position):
    value: int

    def check_neighbors(self, data: list[list[Position]]) -> list["IntPos"]:
        # check if neighbors left and right are int positions
        neighbors: list[IntPos] = []
        #print(data[self.x][self.y])
        #print(data[self.x - 1][self.y ])
        #print(data[self.x + 1][self.y ])
        if check_pos(data, self.x, self.y -1):
            neighbors.append(data[self.x][self.y -1])
        if check_pos(data, self.x, self.y +1):
            neighbors.append(data[self.x][self.y +1])
        for i in neighbors:
            neighbors += i.check_neighbors(data)
        return neighbors

@dataclass
class Symbol(Position):
    symbol: str

    def get_neighbor_pos(self, data: list[list[Position]]) -> list[IntPos]:
        """checks all 8 surrounding positions and returns all positions that are valid"""
        neighbors: list[IntPos] = []
        # guard to avoid out of bounds
        if check_pos(data, self.x - 1, self.y - 1):
            neighbors.append(data[self.x - 1][self.y - 1])
        if check_pos(data, self.x - 1, self.y):
            neighbors.append(data[self.x - 1][self.y])
        if check_pos(data, self.x - 1, self.y + 1):
            neighbors.append(data[self.x - 1][self.y + 1])
        if check_pos(data, self.x, self.y - 1):
            neighbors.append(data[self.x][self.y - 1])
        if check_pos(data, self.x, self.y + 1):
            neighbors.append(data[self.x][self.y + 1])
        if check_pos(data, self.x + 1, self.y - 1):
            neighbors.append(data[self.x + 1][self.y - 1])
        if check_pos(data, self.x + 1, self.y):
            neighbors.append(data[self.x + 1][self.y])
        if check_pos(data, self.x + 1, self.y + 1):
            neighbors.append(data[self.x + 1][self.y + 1])
        return neighbors


@dataclass
class NullPos(Position):
    pass

def read_file():
    with open('test.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]
    
def parse_data():
    raw_data = read_file()
    data = []
    x, y = 0, 0
    for line in raw_data:
        x = 0
        row = []
        for char in line:
            if char == '.':
                row.append(NullPos(x, y))
            elif char != "." and not char.isdigit():
                row.append(Symbol(x, y, char))
            else:
                row.append(IntPos(x, y, int(char)))
            x += 1
        y += 1
        data.append(row)
    return data
    
    




def part1():
    data = parse_data()
    for row in data:
        for col in row:
            if isinstance(col, Symbol):
                for i in col.get_neighbor_pos(data):
                    if isinstance(i, IntPos):
                        neightbors = i.check_neighbors(data)
                        neightbors.append(i)
                        neightbors.sort(key=lambda x: x.x)
                        print("".join([str(i.value) for i in neightbors]))


    #print("Part 1: ", pprint(data))

def part2():
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()