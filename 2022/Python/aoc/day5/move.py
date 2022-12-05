from dataclasses import dataclass


@dataclass
class Move:
    """How many creates to move from the stack to the given stack"""
    amount: int

    """Index of the stack to pick the crates from"""
    from_: int

    """Index of the stack to put the creates to"""
    to: int