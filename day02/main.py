from dataclasses import dataclass
from typing import Mapping

def read_file():
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

@dataclass
class Game:
    id: str
    cubes: Mapping[str, int]


def parse_data():
    data = read_file()
    games: list[Game] = []
    for game_data in data:
        raw_game = game_data.split(':')
        game_id = int(raw_game[0].split(' ')[1])
        cube_chunks = [x.split(",") for x in raw_game[1].split(";")]
        game = Game(game_id, {})
        for chunk in cube_chunks:
            for sc in chunk:
                sub_chunk = sc.strip()
                cube_color = sub_chunk.split(' ')[1]
                cube_count = int(sub_chunk.split(' ')[0])
                if cube_color not in game.cubes or game.cubes[cube_color] < cube_count:
                    game.cubes[cube_color] = cube_count
        games.append(game)
    return games

def part1():
    games = parse_data()
    valid_games: list[Game] = []
    for game in games:
        if game.cubes['red'] <= 12 and game.cubes['green'] <= 13 and game.cubes['blue'] <= 14:
            valid_games.append(game)
    summ: int = 0
    for game in valid_games:
        summ += game.id
    print("Part 1: ", summ)

def part2():
    games = parse_data()
    val: int = 0
    for game in games:
        val += game.cubes['red'] * game.cubes['green'] * game.cubes['blue']
    print("Part 2: ", val)
    

def main():
    part1()
    part2()


if __name__ == "__main__":
    main()