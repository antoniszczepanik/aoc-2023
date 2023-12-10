from typing import List
import sys

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        return file.readlines()

def read_histories(filename: str) -> List[List[int]]:
    return [list(map(int, l.strip().split())) for l in read_lines(filename)]

def solve1(filename: str) -> int:
    histories = read_histories(filename)
    result = 0
    for history in histories:
        diffs = history
        while any(x != 0 for x in diffs):
            result += diffs[-1]
            diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs) - 1)]
    return result

def solve2(filename: str) -> int:
    histories = read_histories(filename)
    result = 0
    for history in histories:
        diffs = history
        firsts = []
        while any(x != 0 for x in diffs):
            firsts.append(diffs[0])
            diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs) - 1)]
        acc = 0
        for first in reversed(firsts):
            acc = first - acc
        result += acc
    return result

print("Day 9:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
