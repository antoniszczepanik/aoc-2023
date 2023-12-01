import sys
from typing import List

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def get_first_digit(line: str) -> str:
    for l in line:
        if l.isdigit():
            return l

def solve1(filename: str) -> int:
    lines = read_lines(filename)
    result = 0
    for line in lines:
        result += int(get_first_digit(line) + get_first_digit(reversed(line)))
    return result

def try_replace_first(line: str, reversed: bool = False) -> str:
    replace = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    min_replace_start, number_to_replace = float('inf'), None
    for to_replace in replace.keys():
        if reversed:
            to_replace = to_replace[::-1]
        ix = line.find(to_replace)
        if ix != -1 and ix < min_replace_start:
            min_replace_start = ix
            number_to_replace = to_replace

    if number_to_replace:
        line = line.replace(number_to_replace, replace[number_to_replace[::-1] if reversed else number_to_replace])
    return line


def solve2(filename: str) -> int:
    lines = read_lines(filename)
    result = 0
    for line in lines:
        first_replaced = try_replace_first(line)
        last_replaced = try_replace_first(line[::-1], reversed=True)
        result += int(get_first_digit(first_replaced) + get_first_digit(last_replaced))
    return result

print("Day 1:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
