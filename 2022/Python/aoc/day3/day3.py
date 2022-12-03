import os.path
import string

from common.base_day import BaseDay
from common.helpers import split_list_in_half


class Day3(BaseDay):
    # Precalculate priorities using the ASCII character codes and offset
    _priorities: dict[str, int] = dict(
        {lowercase: (ord(lowercase) - 96) for lowercase in string.ascii_lowercase} |
        {uppercase: (ord(uppercase) - 38) for uppercase in string.ascii_uppercase}
    )

    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day3")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = input_file.read().splitlines()

    def run_part1(self) -> int:
        duplicate_sum = 0
        for rucksack in self.input:
            first_compartment, second_compartment = split_list_in_half(list(rucksack))
            duplicate_items: set[str] = set([item for item in first_compartment if item in second_compartment])
            duplicate_sum += sum([self._priorities[item] for item in duplicate_items])

        return duplicate_sum

    def run_part2(self) -> int:
        badges_sum = 0
        for elf_group in [self.input[i:i + 3] for i in range(0, len(self.input), 3)]:
            badges: set[str] = set([item for item in elf_group[0] if item in elf_group[1] and item in elf_group[2]])
            badges_sum += sum([self._priorities[item] for item in badges])

        return badges_sum
