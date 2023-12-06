from collections import defaultdict
from dataclasses import dataclass
from typing import List, Callable
import sys

from concurrent.futures import ThreadPoolExecutor

@dataclass
class SubConversion:
    source: int
    destination: int
    length: int

    def check(self, number):
        return self.source <= number < (self.source + self.length)

    def apply(self, number):
        return number + (self.destination - self.source)

@dataclass
class Conversion:
    subconversions: List[SubConversion]

    def apply(self, number):
        for subconversion in self.subconversions:
            if subconversion.check(number):
                return subconversion.apply(number)
        return number

@dataclass
class Almanac:
    seeds: List[int]
    conversions: List[Conversion]

    def apply(self, number):
        for conversion in self.conversions:
            number = conversion.apply(number)
        return number

def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        content = file.read()
    return content

def read_almanac(filename: str) -> Almanac:
    seeds_raw, *conversions_raw = read_file(filename).split("\n\n")
    seeds = list(map(int, seeds_raw.replace("seeds: ", "").split(" ")))
    conversions = []
    for subconversions_raw in conversions_raw:
        subconversions = []
        for subconversion_raw in subconversions_raw.split("\n")[1:]:
            (destination, source, length) = list(map(int, subconversion_raw.split(" ")))
            subconversions.append(SubConversion(source, destination, length))
        conversions.append(Conversion(subconversions))
    return Almanac(seeds, conversions)

def solve1(filename: str) -> int:
    almanac = read_almanac(filename)
    return min(almanac.apply(seed) for seed in almanac.seeds)

def solve2(filename: str) -> int:
    almanac = read_almanac(filename)
    result = float("inf")
    for start, length in zip(almanac.seeds[::2], almanac.seeds[1::2]):
        # :(
        for seed in range(start, start + length):
            result = min(result, almanac.apply(seed))
        print("solved")
    return result

print("Day 5:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
