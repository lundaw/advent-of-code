import os.path

from common.base_day import BaseDay


class Day3(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day3")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = input_file.readline()

    def run_part1(self) -> int:
        visited_houses = self._calculate_visited(list(self.input))
        return len(visited_houses)

    def run_part2(self) -> int:
        santa_visited = self._calculate_visited(list(self.input[::2]))
        robo_santa_visited = self._calculate_visited(list(self.input[1::2]))
        merge = santa_visited.union(robo_santa_visited)

        return len(merge)

    @staticmethod
    def _calculate_visited(directions: list[str]) -> set[(int, int)]:
        x, y = 0, 0
        visited: set[(int, int)] = {(0, 0)}
        for direction in directions:
            match direction:
                case ">":
                    x += 1
                case "<":
                    x -= 1
                case "^":
                    y += 1
                case "v":
                    y -= 1
            visited.add((x, y))

        return visited
