from typing import List, Dict, Callable
from collections import Counter
from dataclasses import dataclass
import sys

@dataclass
class Hand:
    cards: str
    bid: int
    rank: int
    order: Dict[str, int]

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        return [self.order[c] for c in self.cards] < [self.order[c] for c in other.cards]

order_1 = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
def rank_1(cards: str) -> int:
    counts = Counter((Counter(cards).values()))
    if counts[5] == 1:
        return 6
    elif counts[4] == 1:
        return 5
    elif counts[3] == 1 and counts[2] == 1:
        return 4
    elif counts[3] == 1:
        return 3
    elif counts[2] == 2:
        return 2
    elif counts[2] == 1:
        return 1
    return 0

order_2 = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13}
def rank_2(cards: str) -> int:
    js = cards.count("J")
    counts = Counter(Counter(cards.replace("J", "")).values())
    summed = js + (max(counts) if counts else 0)
    if summed >= 5:
        return 6
    if summed == 4:
        return 5
    if (counts[3] == 1 and counts[2] == 1) or (counts[2] == 2 and js == 1):
        return 4
    if summed == 3:
        return 3
    if counts[2] == 2:
        return 2
    if summed == 2:
        return 1
    return 0

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = file.readlines()
    return lines

def read_hands(filename: str, rank: Callable[[str], int], order: Dict[str, int]) -> List[Hand]:
    hands = []
    for line in read_lines(filename):
        cards, bid = line.split(" ")
        hands.append(Hand(cards, int(bid), rank(cards), order))
    return hands

solve = lambda hands: sum(i * h.bid for i, h in enumerate(sorted(hands), 1))

def solve1(filename: str) -> int:
    return solve(read_hands(filename, rank_1, order_1))

def solve2(filename: str) -> int:
    return solve(read_hands(filename, rank_2, order_2))

print("Day 7:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
