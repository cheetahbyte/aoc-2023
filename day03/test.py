from pprint import pprint
from dataclasses import dataclass, asdict

@dataclass
class Position:
    x: int
    y: int


    dict = asdict

    def is_neighbor(self, other: "Position") -> bool:
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

a = [[None, None, 1, 6, None, None, None], [None, -1, None, None, None, None, -1], [4, 3, 5, None, None, None, 2]]


def find_neg_one(dat) -> list[Position]:
    positions: list[Position] = []
    for i in range(len(dat)):
        for j in range(len(dat[i])):
            if dat[i][j] == -1:
                positions.append(Position(i, j))
    return positions

def check_pos(dat, x: int, y: int) -> bool:
    # check if position is out of bounds if so return false
    if x < 0 or y < 0 or x >= len(dat) or y >= len(dat[0]):
        return False
    return dat[x][y] != -1 and type(dat[x][y]) is int

def check_8_surrounding(dat, x: int, y: int) -> bool:
    # check all 8 surrounding positions if they are numbers != 1. if so return all positions that are valid
    abc: list[(int, Position)] = []
    # guard to avoid out of bounds
    if check_pos(dat, x - 1, y - 1):
        abc.append((dat[x - 1][y - 1], Position(x - 1, y - 1)))
    if check_pos(dat, x - 1, y):
        abc.append((dat[x - 1][y], Position(x - 1, y)))
    if check_pos(dat, x - 1, y + 1):
        abc.append((dat[x - 1][y + 1], Position(x - 1, y + 1)))
    if check_pos(dat, x, y - 1):
        abc.append((dat[x][y - 1], Position(x, y - 1)))
    if check_pos(dat, x, y + 1):
        abc.append((dat[x][y + 1], Position(x, y + 1)))
    if check_pos(dat, x + 1, y - 1):
        abc.append((dat[x + 1][y - 1], Position(x + 1, y - 1)))
    if check_pos(dat, x + 1, y):
        abc.append((dat[x + 1][y], Position(x + 1, y)))
    if check_pos(dat, x + 1, y + 1):
        abc.append((dat[x + 1][y + 1], Position(x + 1, y + 1)))
    return abc

def main():
    for pos in find_neg_one(a):
        x = check_8_surrounding(a, pos.x, pos.y)
        print(x)
        print("ENDING")
    
if __name__ == "__main__":
    main()