from typing import List
from dataclasses import dataclass
import sys

@dataclass
class Op:
    label: str
    value: int | None = None

def read(filename: str) -> List[str]:
    with open(filename) as file:
        return file.read().split(",")

def hash(chars: str) -> int:
    curr = 0
    for char in chars:
        curr +=  ord(char)
        curr *=  17
        curr %=  256
    return curr

def solve1(filename: str) -> int:
    return sum([hash(x) for x in read(filename)])

def read_ops(filename: str) -> List[Op]:
    ops = []
    for raw_op in read(filename):
        match raw_op.split("="):
            case [removal]: ops.append(Op(removal[:-1]))
            case [addition, value]: ops.append(Op(addition, int(value)))
            case _: assert False, "unreachable"
    return ops

def solve2(filename: str) -> int:
    boxes = [dict() for _ in range(256)]
    for op in read_ops(filename):
        box = boxes[hash(op.label)]
        if op.value:
            box[op.label] = op.value
        else:
            box.pop(op.label, None)
    result = 0
    for box_n, box in enumerate(boxes, 1):
        for slot_n, value in enumerate(box.values(), 1):
            result += box_n * slot_n * value
    return result

print("Day 15:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
