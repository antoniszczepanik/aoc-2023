from typing import List
import sys

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        return [l.strip() for l in file.readlines()]

def solve1(filename: str) -> int:
    platform = read_lines(filename)
    weight = 0
    for i in range(len(platform[0])):
        start = len(platform)
        for j in range(len(platform)):
            if platform[j][i] == "O":
                print(i, start)
                weight += start
                start -= 1
            elif platform[j][i] == "#":
                start = len(platform) - j - 1
    return weight

def solve2(filename: str) -> int:
    pass

print("Day 14:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
