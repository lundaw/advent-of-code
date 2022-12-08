import os.path

from common.base_day import BaseDay


class Day8(BaseDay):
    _suitable_trees: list[tuple[int, int]] = []

    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, self.__class__.__name__.lower())
        self.input: list[list[int]] = []
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            for line in input_file.read().splitlines():
                self.dimension = len(line) - 1
                self.input.append([int(height) for height in line])

    def run_part1(self) -> int:
        def is_visible(x: int, y: int) -> bool:
            # Check if it is on the edge
            if x == 0 or y == 0 or x == self.dimension or y == self.dimension:
                return True

            # Search from top
            top_visible = True
            for analyzed_y in range(0, y, 1):
                if self.input[analyzed_y][x] >= self.input[y][x]:
                    top_visible = False
                    break

            # Search from bottom
            bottom_visible = True
            for analyzed_y in range(self.dimension, y, -1):
                if self.input[analyzed_y][x] >= self.input[y][x]:
                    bottom_visible = False
                    break

            # Search from left
            left_visible = True
            for analyzed_x in range(0, x, 1):
                if self.input[y][analyzed_x] >= self.input[y][x]:
                    left_visible = False
                    break

            # Search from right
            right_visible = True
            for analyzed_x in range(self.dimension, x, -1):
                if self.input[y][analyzed_x] >= self.input[y][x]:
                    right_visible = False
                    break

            return top_visible or bottom_visible or left_visible or right_visible

        for x in range(0, self.dimension + 1):
            for y in range(0, self.dimension + 1):
                if is_visible(y, x):
                    self._suitable_trees.append((x, y))

        return len(self._suitable_trees)

    def run_part2(self) -> int:
        def calculate_scenic_score(x: int, y: int) -> int:
            if x == 0 or x == self.dimension or y == 0 or y == self.dimension:
                return 0

            # Look towards top
            for analyzed_y in range(y - 1, -1, -1):
                if self.input[analyzed_y][x] >= self.input[y][x]:
                    top_score = y - analyzed_y
                    break
            else:
                top_score = y if y > 0 else 1

            # Look towards bottom
            for analyzed_y in range(y + 1, self.dimension, 1):
                if self.input[analyzed_y][x] >= self.input[y][x]:
                    bottom_score = analyzed_y - y
                    break
            else:
                bottom_score = (self.dimension - y) if y < self.dimension else 1

            # Look towards left
            for analyzed_x in range(x - 1, -1, -1):
                if self.input[y][analyzed_x] >= self.input[y][x]:
                    left_score = x - analyzed_x
                    break
            else:
                left_score = x if x > 0 else 1

            # Look towards right
            for analyzed_x in range(x + 1, self.dimension, 1):
                if self.input[y][analyzed_x] >= self.input[y][x]:
                    right_score = analyzed_x - x
                    break
            else:
                right_score = (self.dimension - x) if x < self.dimension else 1

            return top_score * bottom_score * left_score * right_score

        maximum_scenic_score = 0
        for x, y in self._suitable_trees:
            scenic_score = calculate_scenic_score(y, x)
            if scenic_score > maximum_scenic_score:
                maximum_scenic_score = scenic_score

        return maximum_scenic_score
