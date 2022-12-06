import os.path

from common.base_day import BaseDay


class Day6(BaseDay):
    START_OF_PACKET_LEN = 4
    START_OF_MESSAGE_LEN = 14

    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, self.__class__.__name__.lower())
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = input_file.read()

    def run_part1(self) -> int:
        return self._find_matching_subset(self.START_OF_PACKET_LEN)

    def run_part2(self) -> int:
        return self._find_matching_subset(self.START_OF_MESSAGE_LEN)

    def _find_matching_subset(self, length: int):
        input_length = len(self.input)
        for i in range(0, input_length - length, 1):
            subset = set(self.input[i:i + length])
            if len(subset) == length:
                return i + length

        raise RuntimeError("Somehow couldn't find matching subset")