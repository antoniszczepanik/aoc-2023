from typing import List, Tuple, Dict
import sys
from enum import Enum


class Dir(Enum):
    N = 
    S = 1
    W = 2
    E = 3

class PipeType(Enum):
    EW = 0
    NS = 1
    NE = 2
    NW = 3
    SW = 4
    SE = 5
    GROUND = 6
    START = 7

class Pipe:
    def __init__(self, symbol: str):
        match symbol:
            case "|": self.type = PipeType.NS
            case "-": self.type = PipeType.EW
            case "L": self.type = PipeType.NE
            case "J": self.type = PipeType.NW
            case "7": self.type = PipeType.SW
            case "F": self.type = PipeType.SE
            case ".": self.type = PipeType.GROUND
            case "S": self.type = PipeType.START
            case s: raise ValueError(f"unexpected symbol: {s}")

    def next(self, source: Dir) -> Dir | None:
        match (self.type, source):
            case (PipeType.EW, Dir.W): return Dir.W
            case (PipeType.EW, Dir.E): return Dir.E
            case (PipeType.NS, Dir.N): return Dir.N
            case (PipeType.NS, Dir.S): return Dir.S
            case (PipeType.NE, Dir.S): return Dir.E
            case (PipeType.NE, Dir.W): return Dir.N
            case (PipeType.NW, Dir.S): return Dir.W
            case (PipeType.NW, Dir.E): return Dir.N
            case (PipeType.SW, Dir.N): return Dir.W
            case (PipeType.SW, Dir.E): return Dir.S
            case (PipeType.SE, Dir.N): return Dir.E
            case (PipeType.SE, Dir.W): return Dir.S
            case _:
                return None

    def __repr__(self):
        return f"Pipe({self.type})"

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        return file.readlines()

def read_pipes(filename: str) -> List[List[Pipe]]:
    return [[Pipe(p) for p in l.strip()] for l in read_lines(filename)]

def solve1(filename: str) -> int:
    pipes = read_pipes(filename)

    sys.setrecursionlimit(99999)
    def path_len(x: int, y: int, direction: Dir, so_far: int = 0) -> int:
        if x >= len(pipes) or y >= len(pipes[0]) or x < 0 or y < 0:
            return 0
        source = pipes[x][y]
        if source is None or source.type == PipeType.GROUND:
            return 0
        if source.type == PipeType.START:
            return so_far
        match next_dir := source.next(direction):
            case Dir.N: return path_len(x-1, y, next_dir, so_far + 1)
            case Dir.S: return path_len(x+1, y, next_dir, so_far + 1)
            case Dir.E: return path_len(x, y+1, next_dir, so_far + 1)
            case Dir.W: return path_len(x, y-1, next_dir, so_far + 1)
            case _: return 0

    X, Y = range(len(pipes)), range(len(pipes[0]))
    x, y = [(x, y) for x in X for y in Y if pipes[x][y].type == PipeType.START][0]
    sum_paths = 0
    for dx, dy, dir in [(0, 1, Dir.E), (1, 0, Dir.S), (-1, 0, Dir.N), (0, -1, Dir.W)]:
        sum_paths += path_len(x + dx, y + dy, dir)
    return sum_paths // 4 + 1
    

def solve2(filename: str) -> int:
    pass

print("Day 10:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
