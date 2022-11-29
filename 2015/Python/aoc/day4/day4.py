import os.path
from hashlib import md5

from common.base_day import BaseDay


class Day4(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day4")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = input_file.readline()

    def run_part1(self) -> int:
        return self.find_hash_with_leading_zeros(zero_count=5)

    def run_part2(self) -> int:
        return self.find_hash_with_leading_zeros(zero_count=6)

    def find_hash_with_leading_zeros(self, zero_count: int = 5) -> int:
        secret_key = self.input
        leading_string = "0" * zero_count
        i = 1
        while True:
            md5_hash = md5(f"{secret_key}{i}".encode("UTF-8")).hexdigest()
            if md5_hash.startswith(leading_string):
                return i
            i += 1
