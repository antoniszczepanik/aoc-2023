from typing import List
import sys
from enum import Enum

class Dir(Enum):
    T = 0
    B = 1
    L = 2
    R = 3

def read(filename: str) -> List[str]:
    with open(filename) as file:
        return [l.strip() for l in file.readlines()]

def next(x: int, y: int, d: Dir):
    match d:
        case Dir.T:
            return (x - 1, y)
        case Dir.B:
            return (x + 1, y)
        case Dir.L:
            return (x, y - 1)
        case Dir.R:
            return (x, y + 1)

def solve(grid: List[str], x: int, y: int, d: Dir) -> int:
    seen = set()
    sys.setrecursionlimit(9999) 

    def mark(x: int, y: int, d: Dir):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return
        key = f"{x}-{y}_{d}"
        if key in seen:
            return
        seen.add(key)

        match (d, grid[x][y]):
            case (_, "."):
                new_x, new_y = next(x, y, d)
                return mark(new_x, new_y, d)

            case (Dir.T, "/"):
                new_x, new_y = next(x, y, Dir.R)
                return mark(new_x, new_y, Dir.R)
            case (Dir.B, "/"):
                new_x, new_y = next(x, y, Dir.L)
                return mark(new_x, new_y, Dir.L)
            case (Dir.R, "/"):
                new_x, new_y = next(x, y, Dir.T)
                return mark(new_x, new_y, Dir.T)
            case (Dir.L, "/"):
                new_x, new_y = next(x, y, Dir.B)
                return mark(new_x, new_y, Dir.B)

            case (Dir.T, "\\"):
                new_x, new_y = next(x, y, Dir.L)
                return mark(new_x, new_y, Dir.L)
            case (Dir.B, "\\"):
                new_x, new_y = next(x, y, Dir.R)
                return mark(new_x, new_y, Dir.R)
            case (Dir.R, "\\"):
                new_x, new_y = next(x, y, Dir.B)
                return mark(new_x, new_y, Dir.B)
            case (Dir.L, "\\"):
                new_x, new_y = next(x, y, Dir.T)
                return mark(new_x, new_y, Dir.T)

            case (Dir.L | Dir.R, "-"):
                new_x, new_y = next(x, y, d)
                return mark(new_x, new_y, d)
            case (Dir.T | Dir.B, "-"):
                xl, yl = next(x, y, Dir.L)
                xr, yr = next(x, y, Dir.R)
                mark(xl, yl, Dir.L)
                return mark(xr, yr, Dir.R)

            case (Dir.T | Dir.B, "|"):
                new_x, new_y = next(x, y, d)
                return mark(new_x, new_y, d)
            case (Dir.L | Dir.R, "|"):
                xt, yt = next(x, y, Dir.T)
                xb, yb = next(x, y, Dir.B)
                mark(xt, yt, Dir.T)
                return mark(xb, yb, Dir.B)

            case unexpected:
                assert False, f"unexpected: {unexpected}"
        return

    mark(x, y, d)
    return len(set(x.split("_")[0] for x in seen))

def solve1(filename: str) -> int:
    return solve(read(filename), 0, 0, Dir.R)

def solve2(filename: str) -> int:
    grid, result = read(filename), 0
    for i in range(0, len(grid)):
        result = max(result, solve(read(filename), i, 0, Dir.R))
        result = max(result, solve(read(filename), i, len(grid[0]) - 1, Dir.L))
    for j in range(0, len(grid[0])):
        result = max(result, solve(read(filename), 0, j, Dir.B))
        result = max(result, solve(read(filename), len(grid) - 1, j, Dir.T))
    return result

print("Day 16:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
