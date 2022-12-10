import os.path

from common.base_day import BaseDay
from day9.snake import Snake


class Day9(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, self.__class__.__name__.lower())
        self.input: list[tuple[str, int]] = []
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            for line in input_file:
                direction, step = line.split(" ")
                self.input.append((direction, int(step)))

    def run_part1(self) -> int:
        snake: Snake = Snake(1)
        visited_positions: set[tuple[int, int]] = set()

        for direction, step in self.input:
            visited_positions |= snake.step(direction, step)

        return len(visited_positions)

    def run_part2(self) -> int:
        snake = Snake(10)
        visited_positions: set[tuple[int, int]] = set()

        for direction, step in self.input:
            visited_positions |= snake.step(direction, step)

        return len(visited_positions)
