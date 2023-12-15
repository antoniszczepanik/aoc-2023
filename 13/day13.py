from typing import List
import sys

def read_patterns(filename: str) -> List[List[List[str]]]:
    patterns = []
    with open(filename) as file:
        for pattern in file.read().split("\n\n"):
            patterns.append(list(pattern.split("\n")))
    return patterns

def find_symmetry(pattern: List[List[str]], offby: int):
    for i in range(1, len(pattern)):
        diff = 0
        for d in range(len(pattern)):
            before, after = i-1-d, i+d
            if before < 0 or after >= len(pattern):
                break
            for j in range(len(pattern[before])):
                if pattern[before][j] != pattern[after][j]:
                    diff += 1
        if diff == offby:
            return i
    return 0

def solve(filename: str, offby: int) -> int:
    transpose = lambda X: [list(x) for x in zip(*X)]
    result = 0
    for pattern in read_patterns(filename):
        result += 100 * find_symmetry(pattern, offby)
        result += find_symmetry(transpose(pattern), offby)
    return result

def solve1(filename: str) -> int:
    return solve(filename, offby = 0)

def solve2(filename: str) -> int:
    return solve(filename, offby = 1)

print("Day 13:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
