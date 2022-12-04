from dataclasses import dataclass


@dataclass
class ElfCleaningSection:
    start: int
    finish: int