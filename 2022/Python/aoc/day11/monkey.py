import math
import re
from collections import deque
from typing import Self, Callable


class Monkey:
    worry_level_cap: int | None = None
    all_monkeys: list[Self]

    def __init__(self, data: list[str]):
        self.inspected_item_counter = 0
        self.items = deque(map(lambda i: int(i), data[1].split(":")[1].split(",")))
        match re.search(r"([+*]) (\d+|old)", data[2]).group().split(" "):
            case ["+", "old"]:
                self.operation: Callable[[int], int] = lambda num: num + num
            case ["+", amount]:
                self.operation: Callable[[int], int] = lambda num: num + int(amount)
            case ["*", "old"]:
                self.operation: Callable[[int], int] = lambda num: num * num
            case ["*", amount]:
                self.operation: Callable[[int], int] = lambda num: num * int(amount)
        self.divisor = int(data[3].split("by")[1])
        self.true_next_monkey = int(data[4].split("monkey")[1])
        self.false_next_monkey = int(data[5].split("monkey")[1])

    def round(self, relieved=True) -> None:
        assert Monkey.worry_level_cap is not None

        while len(self.items) > 0:
            item = self.operation(self.items.popleft()) % Monkey.worry_level_cap
            if relieved:
                item = math.floor(item / 3)

            next_monkey = self.true_next_monkey if item % self.divisor == 0 else self.false_next_monkey
            Monkey.all_monkeys[next_monkey].items.append(item)

            self.inspected_item_counter += 1
