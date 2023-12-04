from dataclasses import dataclass


def read_file():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]



@dataclass
class Card:
    num: int
    winning_cards: list[int]
    cards: list[int]

    def common_members(self) -> list[int]:
        winning_set = set(self.winning_cards)
        cards_set = set(self.cards)
        return list(winning_set&cards_set)

def parse_data() -> list[Card]:
    raw_data = read_file()
    cards = [
        Card(
            int(raw_card.split(":")[0].split(" ")[-1]),
            [int(i) for i in raw_card.split(":")[1].split("|")[0].split() if i.isdigit()],
            [int(i) for i in raw_card.split(":")[1].split("|")[1].split() if i.isdigit()]
        )
        for raw_card in raw_data
    ]
    return cards

def part1():
    cards = parse_data()
    sum = 0
    for card in cards:
        sum += int(1 * pow(2, len(card.common_members())-1))
    print("Part 1:", sum)


def part2():
    cards = parse_data()
    todo_cards: list[Card] = cards + []
    i = 0
    while i < len(todo_cards):
        card = todo_cards[i]
        wins: int = len(card.common_members())
        if (wins > 0):
            todo_cards += cards[card.num:card.num+wins]
        i+=1
    print("Part 2: ", len(todo_cards))



def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
