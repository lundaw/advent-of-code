import os.path

from common.base_day import BaseDay


class Day1(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day1")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = input_file.read().splitlines()

    def run_part1(self) -> int:
        pass

    def run_part2(self) -> int:
        pass
