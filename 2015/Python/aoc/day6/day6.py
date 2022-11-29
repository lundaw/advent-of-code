import os.path
import re

from common.base_day import BaseDay


class Day6(BaseDay):
    def __init__(self):
        self.regex = re.compile(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)")
        super().__init__()

    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day6")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.raw_input = input_file.read().splitlines()

    def run_part1(self) -> int:
        light_statuses = [[0 for x in range(1000)] for y in range(1000)]
        for line in self.raw_input:
            matches = self.regex.match(line).groups()
            for x in range(int(matches[1]), int(matches[3]) + 1):
                for y in range(int(matches[2]), int(matches[4]) + 1):
                    match matches[0]:
                        case "turn on":
                            light_statuses[x][y] = 1
                        case "turn off":
                            light_statuses[x][y] = 0
                        case "toggle":
                            light_statuses[x][y] = 1 - light_statuses[x][y]

        return sum(sum(light_statuses, []))

    def run_part2(self) -> int:
        light_statuses = [[0 for x in range(1000)] for y in range(1000)]
        for line in self.raw_input:
            matches = self.regex.match(line).groups()
            for x in range(int(matches[1]), int(matches[3]) + 1):
                for y in range(int(matches[2]), int(matches[4]) + 1):
                    match matches[0]:
                        case "turn on":
                            light_statuses[x][y] += 1
                        case "turn off":
                            light_statuses[x][y] = max(0, light_statuses[x][y] - 1)
                        case "toggle":
                            light_statuses[x][y] += 2

        return sum(sum(light_statuses, []))
