import os.path
import re

from common.base_day import BaseDay
from day4.elf_cleaning_section import ElfCleaningSection


class Day4(BaseDay):
    def _parse_input(self) -> None:
        elf_regex = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
        input_path = os.path.join(self.input_root_folder, "day4")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input: list[tuple[ElfCleaningSection, ElfCleaningSection]] = []
            for line in input_file.read().splitlines():
                groups = elf_regex.match(line).groups()
                assert len(groups) == 4

                sections = (
                    ElfCleaningSection(start=int(groups[0]), finish=int(groups[1])),
                    ElfCleaningSection(start=int(groups[2]), finish=int(groups[3]))
                )
                assert len(sections) == 2

                self.input.append(sections)

    def run_part1(self) -> int:
        def is_full_overlap(pair: tuple[ElfCleaningSection, ElfCleaningSection]) -> bool:
            first_elf, second_elf = pair
            assert first_elf.start <= first_elf.finish
            assert second_elf.start <= second_elf.finish

            return (first_elf.start <= second_elf.start and first_elf.finish >= second_elf.finish) \
                or (second_elf.start <= first_elf.start and second_elf.finish >= first_elf.finish)

        return len(list(filter(lambda p: is_full_overlap(p), self.input)))

    def run_part2(self) -> int:
        def is_overlapped(pair: tuple[ElfCleaningSection, ElfCleaningSection]) -> bool:
            first_elf, second_elf = pair
            assert first_elf.start <= first_elf.finish
            assert second_elf.start <= second_elf.finish

            return (first_elf.finish >= second_elf.start >= first_elf.start) \
                or (second_elf.finish >= first_elf.start >= second_elf.start)

        return len(list(filter(lambda p: is_overlapped(p), self.input)))
