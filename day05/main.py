from pprint import pprint
from dataclasses import dataclass


def read_file():
    with open("test.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line != "\n"]


@dataclass
class Seed:
    id: int
    course: list[tuple[str, int]]


@dataclass
class Destination:
    name: str
    start: int
    end: int
    range: int


@dataclass
class Source:
    name: str
    start: int
    end: int
    range: int


@dataclass
class InstructionMap:
    dest: list[Destination]
    source: list[Source]


@dataclass
class Garden:
    seeds: list[Seed]
    instructions: list[tuple[Source, Destination]]


def parse_data() -> Garden:
    raw_data = read_file()
    seeds = [Seed(int(s), [("seed", int(s))]) for s in raw_data[0].split(" ")[1:]]
    raw_map: dict[str, list[str]] = {}
    cur: dict[str, list[int]] = ""
    for r in raw_data[1:]:
        if not r[0].isdigit():
            cur = f'{r.split(" ")[0].split("-")[0]},{r.split(" ")[0].split("-")[2] }'
            raw_map[cur] = []
        else:
            raw_map[cur].append([int(i) for i in r.split(" ")])
    instructions = []
    for k, v in raw_map.items():
        for i in v:
            dest = Destination(k.split(",")[1], i[0], i[0] + i[2], i[2])
            source = Source(k.split(",")[0], i[1], i[1] + i[2], i[2])
            instructions.append((source, dest))

    return Garden(seeds, instructions)


def part1():
    garden = parse_data()
    for source, dest in garden.instructions:
        for seed in garden.seeds:
            # check if is in source range
            if seed.id in range(source.start, source.end):
                # distance from start of source to seed
                offset = abs(source.start - seed.id)
                if not dest.name in [s[0] for s in seed.course]:
                    seed.id = dest.start + offset
                    seed.course.append((dest.name, seed.id))
    # filter smallest id
    smallest = min([s.id for s in garden.seeds])
    print("Part 1:", smallest)


def part2():
    garden = parse_data()
    seeds = garden.seeds.copy()
    new_seeds: list[int] = []
    for pair in list(zip(seeds[::2], seeds[1::2])):
        r = range(pair[0].id +1, pair[0].id + pair[1].id)
        # remove original seeds
        print(r)
        for i in r:
            new_seeds.append(i)
        # break if none of the originals are in garden.seeds
    seeds = new_seeds
    for source, dest in garden.instructions:
        for seed in seeds:
            # check if is in source range
            if seed in range(source.start, source.end):
                # distance from start of source to seed
                offset = abs(source.start - seed)
                seed = dest.start + offset
    # filter smallest id
    smallest = min(seeds)
    print("Part 2:", smallest)
    


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
