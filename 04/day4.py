from collections import defaultdict
from dataclasses import dataclass
from typing import List, Set
import sys

@dataclass
class Card:
    winning: Set[int]
    owned: Set[int]

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def read_cards(filename: str) -> List[Card]:
    to_set = lambda raw: set(map(int, filter(lambda n: len(n) > 0, raw.split(" "))))
    cards = []
    for line in read_lines(filename):
        winning_raw, owned_raw = line.split(": ")[1].split(" | ")
        cards.append(Card(to_set(winning_raw), to_set(owned_raw)))
    return cards

def solve1(filename: str) -> int:
    result = 0
    for card in read_cards(filename):
        wins = len(card.winning.intersection(card.owned))
        if wins != 0:
            result += 2 ** (wins - 1)
    return result

def solve2(filename: str) -> int:
    cards = read_cards(filename)
    counts = {i: 1 for i in range(len(cards))}
    for i, card in enumerate(cards):
        wins = len(card.winning.intersection(card.owned))
        for to_mark in range(i+1, i+1+wins):
            counts[to_mark] += counts[i]
    return sum(v for v in counts.values())

print("Day 4:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
