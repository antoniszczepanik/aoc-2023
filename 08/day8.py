from typing import List, Iterator, Callable
import math
import sys
from dataclasses import dataclass

@dataclass
class Node:
    label: str
    left: 'Node' = None
    right: 'Node' = None

@dataclass
class Documentation:
    nodes: List[Node]
    instructions: List[str]

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = file.readlines()
    return lines

def read_documentation(filename: str) -> Documentation:
    instructions, _, *mappings = read_lines(filename)
    nodes = {}
    for mapping in mappings:
        source, left, right = mapping.replace("= ", "").replace("(", "").replace(",", "").replace(")", "").split()
        for n in (source, left, right):
            if n not in nodes:
                nodes[n] = Node(n)
        nodes[source].left = nodes[left]
        nodes[source].right = nodes[right]
    return Documentation(list(nodes.values()), list(instructions.strip()))

def cycle(a: List[str]) -> Iterator[str]:
    while 1:
        for i in a: yield i

def count_steps(start: Node, instructions: List[str], is_target: Callable[[Node], bool]):
    instructions = cycle(instructions)
    node, steps = start, 0
    while not is_target(node):
        direction = next(instructions)
        match direction:
            case "L":
                node = node.left
            case "R":
                node = node.right
        steps += 1
    return steps

def solve1(filename: str) -> int:
    docs = read_documentation(filename)
    start = [n for n in docs.nodes if n.label == "AAA"][0]
    return count_steps(start, docs.instructions, lambda n: n.label == "ZZZ")

def solve2(filename: str) -> int:
    docs = read_documentation(filename)
    starts = [n for n in docs.nodes if n.label[-1] == "A"]
    return math.lcm(*[count_steps(n, docs.instructions, lambda n: n.label[-1] == "Z") for n in starts])

print("Day 8:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
