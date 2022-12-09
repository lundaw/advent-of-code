import os.path

from common.base_day import BaseDay
from day9.position import Position


class Day9(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, self.__class__.__name__.lower())
        self.input: list[tuple[str, int]] = []
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            for line in input_file:
                direction, step = line.split(" ")
                self.input.append((direction, int(step)))

    def run_part1(self) -> int:
        pos_head = Position(0, 0)
        pos_tail = Position(0, 0)
        visited_positions: set[tuple[int, int]] = set()

        for direction, step in self.input:
            for _ in range(0, step):
                previous_pos_head = Position(pos_head.x, pos_head.y)

                match direction:
                    case "R":
                        pos_head.x += 1
                    case "L":
                        pos_head.x -= 1
                    case "U":
                        pos_head.y += 1
                    case "D":
                        pos_head.y -= 1

                if abs(pos_head.x - pos_tail.x) > 1 or abs(pos_head.y - pos_tail.y) > 1:
                    pos_tail = previous_pos_head
                    visited_positions.add((pos_tail.x, pos_tail.y))

        # Adding plus one for the start position
        return len(visited_positions) + 1

    def run_part2(self) -> int:
        pass
