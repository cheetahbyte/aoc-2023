from dataclasses import dataclass

CARD_VALUES: dict[str, int] = {
    "A": 15,
    "K": 14,
    "Q": 13,
    "J": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    def __init__(self, counter: int, cards: list[str], bid: int) -> None:
        self.rank = counter
        self.cards = cards
        self.bid = bid

    @staticmethod
    def sort_cards(cards: list[str]) -> list[str]:
        return sorted(cards, key=lambda x: CARD_VALUES[x], reverse=True)

    def check_five_of_a_kind(self) -> bool:
        cards = Hand.sort_cards(self.cards)
        return cards[0] == cards[1] == cards[2] == cards[3] == cards[4]

    def check_four_of_a_kind(self) -> bool:
        cards = Hand.sort_cards(self.cards)
        return (
            cards[0] == cards[1] == cards[2] == cards[3]
            or cards[1] == cards[2] == cards[3] == cards[4]
        )

    def check_full_house(self) -> bool:
        cards = Hand.sort_cards(self.cards)
        return cards[0] == cards[1] == cards[2] and cards[3] == cards[4]

    def check_three_of_a_kind(self) -> bool:
        cards = Hand.sort_cards(self.cards)
        return (
            cards[0] == cards[1] == cards[2]
            or cards[1] == cards[2] == cards[3]
            or cards[2] == cards[3] == cards[4]
        )

    def check_two_pairs(self) -> bool:
        cards = Hand.sort_cards(self.cards)
        return (
            cards[0] == cards[1]
            and cards[2] == cards[3]
            or cards[0] == cards[1]
            and cards[3] == cards[4]
            or cards[1] == cards[2]
            and cards[3] == cards[4]
        )

    def check_one_pair(self) -> bool:
        cards = Hand.sort_cards(self.cards)
        return (
            cards[0] == cards[1]
            or cards[1] == cards[2]
            or cards[2] == cards[3]
            or cards[3] == cards[4]
        )
    
    def replace_cards(self) -> list[int]:
        return [CARD_VALUES[x] for x in self.cards]
    

    def __repr__(self) -> str:
        return f"Hand({self.rank}, {self.cards}, {self.bid})"


def read_file():
    with open("test.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line != "\n"]


def parse_data() -> list[tuple[Hand, int]]:
    d = []
    raw_data = read_file()
    c: int = 1
    for row in raw_data:
        d.append(
            Hand(c ,[x for x in row.split(" ")[0].strip()], int(row.split(" ")[1].strip()))
        )
        c += 1
    return d


def part1():
    data = parse_data()

    types = {
        "5": [],
        "4": [],
        "FH": [],
        "3": [],
        "2P": [],
        "1P": [],
        "HC": [],
    }

    for hand in data:
        if hand.check_five_of_a_kind():
            types["5"].append(hand)
        elif hand.check_four_of_a_kind():
            types["4"].append(hand)
        elif hand.check_full_house():
            types["FH"].append(hand)
        elif hand.check_three_of_a_kind():
            types["3"].append(hand)
        elif hand.check_two_pairs():
            types["2P"].append(hand)
        elif hand.check_one_pair():
            types["1P"].append(hand)
        else:
            types["HC"].append(hand)

    for (typ, hands) in types.items():
        sorted_hands = sorted(hands, key=lambda x: x.replace_cards(), reverse=False)
        types[typ] = sorted_hands

    val: int = 0
    cnt: int = 1


    for (t, hands) in types.items().__reversed__():
        print(t, len(hands))
        for hand in hands:
            val += hand.bid * cnt
            cnt += 1
            

    print("Part 1:", val)
        
            






def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
