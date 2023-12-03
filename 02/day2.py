from collections import Counter
from dataclasses import dataclass
from typing import List
import sys

@dataclass
class Cubes:
    red: int = 0
    blue: int = 0
    green: int = 0

    def add(self, color: str, amount: int):
        match color:
            case "red": self.red += amount
            case "blue": self.blue += amount
            case "green": self.green += amount

    def can_be_drawn_from(self, pool):
        return self.red <= pool.red and self.blue <= pool.blue and self.green <= pool.green

    def max(self, other):
        return Cubes(red = max(self.red, other.red), blue = max(self.blue, other.blue), green = max(self.green, other.green))

    def power(self):
        return self.red * self.blue * self.green

class Game:
    def __init__(self, game_id: int):
        self.game_id = game_id
        self.reveals = []

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def read_games(filename: str) -> int:
    lines = read_lines(filename)
    games = []
    for line in lines:
        (game, reveals) = line.split(": ")
        (_, game_id) = game.split(" ")
        new_game = Game(int(game_id))
        for reveal in reveals.split(";"):
            cubes = Cubes()
            for item in reveal.split(", "):
                (count, color) = item.strip().split(" ")
                cubes.add(color, int(count))
            new_game.reveals.append(cubes)
        games.append(new_game)
    return games

def solve1(filename: str) -> int:
    games = read_games(filename)
    cube_pool = Cubes(red = 12, green = 13, blue = 14)
    result = 0
    for game in games:
        for reveal in game.reveals:
            if not reveal.can_be_drawn_from(cube_pool): break
        else:
            result += game.game_id
    return result

def solve2(filename: str) -> int:
    games = read_games(filename)
    result = 0
    for game in games:
        mins = Cubes()
        for reveal in game.reveals:
            mins = reveal.max(mins)
        result += mins.power()
    return result

print("Day 2:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
