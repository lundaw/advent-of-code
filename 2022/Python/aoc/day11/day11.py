import copy
import math
import os.path

from common.base_day import BaseDay
from day11.monkey import Monkey


class Day11(BaseDay):
    def _parse_input(self) -> None:
        self.monkeys: list[Monkey] = []
        input_path = os.path.join(self.input_root_folder, self.__class__.__name__.lower())
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.monkeys = [Monkey(monkey.splitlines()) for monkey in input_file.read().split("\n\n")]
        Monkey.worry_level_cap = math.prod(monkey.divisor for monkey in self.monkeys)

    def run_part1(self) -> int:
        Monkey.all_monkeys = copy.deepcopy(self.monkeys)

        for _ in range(20):
            for monkey in Monkey.all_monkeys:
                monkey.round()

        return math.prod(sorted(map(lambda m: m.inspected_item_counter, Monkey.all_monkeys), reverse=True)[:2])

    def run_part2(self) -> int:
        Monkey.all_monkeys = copy.deepcopy(self.monkeys)

        for i in range(10_000):
            for monkey in Monkey.all_monkeys:
                monkey.round(relieved=False)

        return math.prod(sorted(map(lambda m: m.inspected_item_counter, Monkey.all_monkeys), reverse=True)[:2])