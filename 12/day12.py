from typing import List, Tuple
from dataclasses import dataclass
from functools import cache
import sys

@dataclass
class Record:
    springs: str
    groups: Tuple[int]

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        return [l.strip() for l in file.readlines()]

def read_records(filename: str):
    records = []
    for l in read_lines(filename):
        springs, groups = l.split()
        records.append(Record(springs, tuple(map(int, groups.split(",")))))
    return records

@cache
def count(springs: Tuple[str], groups: Tuple[int]) -> int:
    if not springs:
        return 1 if not groups else 0
    if not groups:
        return 1 if "#" not in springs else 0
    if springs[0] == ".":
        return count(springs[1:], groups)

    size = groups[0]
    if len(springs) < size:
        return 0

    result = 0
    if springs[0] == "?":
        result += count(springs[1:], groups)

    next = springs[size] if size < len(springs) else "."
    if all([s in "#?" for s in springs[:size]]) and next in ("?."):
        result += count(springs[size + 1:], groups[1:])

    return result

def solve1(filename: str) -> int:
    return sum(count(tuple(r.springs), r.groups)  for r in read_records(filename))

def solve2(filename: str) -> int:
    return sum(count(tuple("?".join([r.springs] * 5)), r.groups * 5)  for r in read_records(filename))

print("Day 12:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
