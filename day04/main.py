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
    cards = []
    for raw_card in raw_data:
        raw_split_card = raw_card.split(":")
        cid: int = int(raw_split_card[0].split(" ")[-1])
        raw_cards_sec = raw_split_card[1].split("|")
        cards.append(
            Card(
                cid,
                [int(i) for i in raw_cards_sec[0].split(" ") if i.isdigit()],
                [int(i) for i in raw_cards_sec[1].split(" ") if i.isdigit()],
            )
        )
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
