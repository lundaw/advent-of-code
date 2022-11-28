import os.path

from common.base_day import BaseDay


class Day1(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day1")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = input_file.readline()

    def run_part1(self) -> int:
        downwards = self.input.count(')')
        upwards = self.input.count('(')

        return upwards - downwards

    def run_part2(self) -> int:
        floor: int = 0
        for index, step in enumerate(self.input, 1):
            floor = floor + (1 if step == '(' else -1)

            if floor < 0:
                return index
