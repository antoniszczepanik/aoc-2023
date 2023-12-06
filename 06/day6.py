from typing import List
from dataclasses import dataclass
import sys

@dataclass
class Sheet:
    times: List[int]
    distances: List[int]

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = file.readlines()
    return lines

def read_sheet(filename: str) -> Sheet:
    clean_line = lambda line, remove: list(map(int, filter(lambda i: len(i) > 0, line.replace(remove, "").split(" "))))
    time_line, distance_line = read_lines(filename)
    return Sheet(clean_line(time_line, "Time:"), clean_line(distance_line, "Distance:"))

def solve1(filename: str) -> int:
    sheet = read_sheet(filename)
    result = 1
    for time, distance in zip(sheet.times, sheet.distances):
        result *= sum(1 if (time - ms) * ms > distance else 0 for ms in range(time + 1))
    return result

def solve2(filename: str) -> int:
    sheet = read_sheet(filename)
    join = lambda nums: int("".join(map(str, nums)))
    time, distance = join(sheet.times), join(sheet.distances)
    return sum(1 if (time - ms) * ms > distance else 0 for ms in range(time + 1))

def find_start(time: int, distance: int):
    low, hi = 0, time
    while low <= hi:
        mid = (low + hi) // 2
        mid_value = (time + 1 - mid) * mid
        mid_next_value = (time - mid) * (mid + 1)
        if mid_value <= distance and mid_next_value > distance:
            return mid + 1
        elif mid_value < distance:
            low = mid + 1
        else:
            hi = mid - 1
    return -1

def find_end(time: int, distance: int):
    low, hi = 0, time
    while low <= hi:
        mid = (low + hi) // 2
        mid_value = (time + 1 - mid) * mid
        mid_next_value = (time - mid) * (mid + 1)
        if mid_value > distance and mid_next_value <= distance:
            return mid
        elif mid_value > distance:
            low = mid + 1
        else:
            hi = mid - 1
    return -1

def solve2_star(filename: str) -> int:
    sheet = read_sheet(filename)
    join = lambda nums: int("".join(map(str, nums)))
    time, distance = join(sheet.times), join(sheet.distances)
    return find_end(time, distance) - find_start(time, distance)

print("Day 6:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
print(f"  Part 2*: {solve2_star(sys.argv[1])}")
