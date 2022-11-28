import os.path

from common.base_day import BaseDay
from day2.box_dimension import BoxDimension


class Day2(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day2")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = [
                BoxDimension(*map(lambda s: int(s), line.strip().split("x"))) for line in input_file.readlines()
            ]

    def run_part1(self) -> int:
        return sum([box.get_wrapping_paper_length() for box in self.input])

    def run_part2(self) -> int:
        return sum([box.get_ribbon_length() for box in self.input])
