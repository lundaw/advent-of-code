from dataclasses import dataclass


@dataclass
class Node:
    x: int
    y: int
    height: int
    steps: int = 0
