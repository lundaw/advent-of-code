import functools
import os.path

from common.base_day import BaseDay


class Day1(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day1")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = [functools.reduce(
                lambda accumulator, current: accumulator + int(current), line.splitlines(), 0
            ) for line in input_file.read().split("\n\n")]

    def run_part1(self) -> int:
        return max(self.input)

    def run_part2(self) -> int:
        sorted_ = self.input.copy()
        sorted_.sort(reverse=True)

        return sum(sorted_[:3])
