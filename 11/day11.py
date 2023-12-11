from typing import List
import sys

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        return [l.strip() for l in file.readlines()]

def read_points(filename: str) -> List[str]:
    lines = read_lines(filename)
    points = []
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == "#":
                points.append((x, y))
    return points, len(lines), len(lines[0])

def solve(filename: str, multiplier: int) -> int:
    points, x, y = read_points(filename)
    row_mask, col_mask = [1 for _ in range(x)], [1 for _ in range(y)]
    for x, y in points:
        row_mask[x], col_mask[y] = 0, 0

    result = 0
    for i in range(len(points)):
        for j in range(i, len(points)):
            (x1, y1), (x2, y2) = points[i], points[j]
            (x1, x2), (y1, y2) = sorted([x1, x2]), sorted([y1, y2])
            result += (x2 - x1) + (y2 - y1)
            empty = sum(row_mask[x1:x2+1]) + sum(col_mask[y1:y2+1])
            result += (multiplier - 1) * empty
    return result

def solve1(filename: str) -> int:
    return solve(filename, multiplier = 2)

def solve2(filename: str) -> int:
    return solve(filename, multiplier = 1_000_000)

print("Day 11:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
