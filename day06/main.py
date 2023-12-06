
def distance(holding_time: int, time: int) -> int:
    speed: int = holding_time
    rest_time: int = time - holding_time
    return rest_time * speed


def read_file():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line != "\n"]
    
def parse_data() -> tuple[list[int], list[int]]:
    raw_data = read_file()
    time, distance = [int(i) for i in raw_data[0][5:].strip().split(" ") if i != ""], [int(i) for i in raw_data[1][9:].strip().split(" ") if i != ""]
    return time, distance

def parse_data2() -> tuple[int, int]:
    raw_data = read_file()
    time, distance = int(raw_data[0][5:].strip().replace(" ", "")), int(raw_data[1][9:].strip().replace(" ", ""))
    return time, distance

def part1():
    data = parse_data()
    mul: int = 1
    for race in zip(data[0], data[1]):
        possibilities: list[int] = []
        goal: int = race[1]
        total_time: int = race[0]
        for i in range(total_time-1):
            if distance(i, total_time) > goal:
                possibilities.append(i)
        mul *= len(possibilities)
    print("Part 1:", mul)

def part2():
    data = parse_data2()
    possibilities: list[int] = []
    for i in range(data[0]):
        if distance(i, data[0]) > data[1]:
            possibilities.append(i)
    print("Part 2:", len(possibilities))


def part2_alt():
    data = parse_data2()
    start, end = 0, 0
    # increase start until distance(start, data[0]) > data[1]
    # increase end until distance(end, data[0]) > data[1]
    # end - start = answer
    # start = 0
    # end = 0
    while distance(start, data[0]) < data[1]:
        start += 1
    while distance(data[0] - end, data[0]) < data[1]:
        end += 1

    print(start, end)
    
def main():
    part1()
    part2_alt()

if __name__ == "__main__":
    main()
