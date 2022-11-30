import os
import pathlib
from abc import abstractmethod


class BaseDay:
    year: int = 2022
    input_root_folder = os.path.join(pathlib.Path(os.getcwd()).parents[2], "_inputs", str(year))

    def __init__(self):
        self._parse_input()

    def __call__(self, *args, **kwargs) -> tuple[int, int]:
        part1 = self.run_part1()
        part2 = self.run_part2()

        return part1, part2

    @abstractmethod
    def _parse_input(self) -> None:
        pass

    @abstractmethod
    def run_part1(self) -> int:
        pass

    @abstractmethod
    def run_part2(self) -> int:
        pass
