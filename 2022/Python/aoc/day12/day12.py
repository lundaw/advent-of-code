import os.path

from aoc.common.base_day import BaseDay


class Day12(BaseDay):
    node_steps: dict[tuple[int, int]] = {}

    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, self.__class__.__name__.lower())
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.heightmap = [list(map(ord, line.strip())) for line in input_file.readlines()]

        self.height = len(self.heightmap)
        self.width = len(self.heightmap[0])

        for i in range(self.height):
            for j in range(self.width):
                if self.heightmap[i][j] == ord("S"):
                    self.start_coordinate = (i, j)
                elif self.heightmap[i][j] == ord("E"):
                    self.end_coordinate = (i, j)
        self.heightmap[self.start_coordinate[0]][self.start_coordinate[1]] = ord("a")
        self.heightmap[self.end_coordinate[0]][self.end_coordinate[1]] = ord("z")
        self.node_steps[self.end_coordinate] = 0

        self._run_bfs()

    def run_part1(self) -> int:
        return self.node_steps[self.start_coordinate]

    def run_part2(self) -> int:
        starting_points = [(x, y) for x in range(self.height) for y in range(self.width) if
                           self.heightmap[x][y] == ord("a")]

        return min([self.node_steps[(x, y)] for x, y in starting_points if (x, y) in self.node_steps])

    def _run_bfs(self) -> None:
        visited: list[tuple[int, int]] = []
        queue: list[tuple[int, int]] = []

        visited.append(self.end_coordinate)
        queue.append(self.end_coordinate)

        while len(queue) > 0:
            current = queue.pop(0)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = current[0] + dx, current[1] + dy
                if 0 <= nx < self.height and 0 <= ny < self.width \
                        and (nx, ny) not in visited \
                        and (self.heightmap[current[0]][current[1]] - self.heightmap[nx][ny]) <= 1:
                    neighbour_tuple = (nx, ny)
                    visited.append(neighbour_tuple)
                    queue.append(neighbour_tuple)
                    self.node_steps[neighbour_tuple] = self.node_steps[current] + 1
