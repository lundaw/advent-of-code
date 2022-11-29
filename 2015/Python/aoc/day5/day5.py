import os.path
import re
import string

from common.base_day import BaseDay


class Day5(BaseDay):
    forbidden_substrings: list[str] = ["ab", "cd", "pq", "xy"]
    vowels: list[str] = list("aeiou")
    double_letters: list[str] = list(map(lambda l: l * 2, string.ascii_lowercase))

    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day5")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = input_file.read().splitlines()

    def run_part1(self) -> int:
        def is_nice_string(analysed_string: str) -> bool:
            # Criteria #3: does not contain forbidden strings ('ab', 'cd', 'pq', 'xy')
            if any(forbidden_substring in analysed_string for forbidden_substring in self.forbidden_substrings):
                return False

            # Criteria #1: has at least 3 vowels. Voewls does not have to be different, just count
            if sum(analysed_string.count(vowel) for vowel in self.vowels) < 3:
                return False

            # Criteria #2: has letters that appear twice in a row, like 'aa' or 'zz'
            if not any(double_letter in analysed_string for double_letter in self.double_letters):
                return False

            return True

        return len(list(filter(lambda l: is_nice_string(l), self.input)))

    def run_part2(self) -> int:
        def is_nice_string(analysed_string: str) -> bool:
            # Criteria #1: contains a pair of two letters appearing twice, without overlap
            if not re.search(r"([a-z][a-z]).*\1", analysed_string):
                return False

            # Criteria #2: contains a letter that repeats after a character between, like 'axa', 'zaz' or 'aaa'
            if not re.search(r"([a-z]).\1", analysed_string):
                return False

            return True

        return len(list(filter(lambda l: is_nice_string(l), self.input)))
