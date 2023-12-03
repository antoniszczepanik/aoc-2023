from dataclasses import dataclass
from typing import List, Set
import sys

@dataclass
class Number:
    value: int
    start_x: int
    start_y: int
    length: int

    def __hash__(self):
        return hash(self.value) + hash(self.start_x) + hash(self.start_y) + hash(self.length)

@dataclass
class Gear:
    x: int
    y: int

class ValidLocations:

    def __init__(self, schema):
        self.x_limit = len(schema)
        self.y_limit = len(schema[0])
        self.locations = set()
        for x in range(self.x_limit):
            for y in range(self.y_limit):
                l = schema[x][y]
                if l != "." and not l.isdigit():
                    self.add(x, y)

    def add(self, x, y):
        for loc in adjacent_for(x, y):
            if loc[0] >= 0 and loc[0] < self.x_limit and loc[1] >= 0 and loc[1] < self.y_limit:
                self.locations.add(loc)

    def is_valid(self, x, y, length):
        for y2 in range(y, y + length):
            if (x, y2) in self.locations:
                return True
        return False

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def adjacent_for(x: int, y: int) -> Set[tuple[int, int]]:
    return {
        (x - 1, y),
        (x, y - 1),
        (x - 1, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
    }

def get_numbers(schema: str) -> List[Number]:
    numbers = []
    for x, line in enumerate(schema):
        start_y = None
        digits = []
        for y, l in enumerate(line):
            if l.isdigit():
                if start_y is None:
                    start_y = y
                digits.append(l)
            if start_y is not None and (not l.isdigit() or y == len(line) - 1):
                numbers.append(Number(int("".join(digits)), x, start_y, len(digits)))
                start_y = None
                digits = []
    return numbers

def solve1(filename: str) -> int:
    schema = read_lines(filename)
    valid_locations = ValidLocations(schema)
    result = 0
    for number in get_numbers(schema):
        if valid_locations.is_valid(number.start_x, number.start_y, number.length):
            result += number.value
    return result

def get_gears(schema: List[List[str]]) -> List[Gear]:
    gears = []
    for x in range(len(schema)):
        for y in range(len(schema[0])):
            if schema[x][y] == "*":
                gears.append(Gear(x, y))
    return gears

def find_adjacent(numbers: List[Number], gear: Gear) -> List[Number]:
    adjacent = adjacent_for(gear.x, gear.y)
    adjacent_numbers = set()
    for number in numbers:
        for y in range(number.start_y, number.start_y + number.length):
            if (number.start_x, y) in adjacent:
                adjacent_numbers.add(number)
    return adjacent_numbers
    
def solve2(filename: str) -> int:
    schema = read_lines(filename)
    gears = get_gears(schema)
    numbers = get_numbers(schema)
    result = 0
    for gear in gears:
        adjacent = find_adjacent(numbers, gear)
        if len(adjacent) == 2:
            result += adjacent.pop().value * adjacent.pop().value
    return result

print("Day 3:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
