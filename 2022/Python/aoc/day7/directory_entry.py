from builtins import int
from dataclasses import dataclass, field
from typing import Self


@dataclass
class DirectoryEntry:
    name: str

    parent: Self | None = None

    subdirectories: dict[str, Self] = field(default_factory=dict)

    """Sum of the sizes of the files in the directory. Does not account for subdirectories."""
    size: int = 0

    recursive_size: int | None = None

    def calculate_recursive_size(self):
        self.recursive_size = self.size
        for subdirectory in self.subdirectories.values():
            if subdirectory.recursive_size is None:
                subdirectory.calculate_recursive_size()
            self.recursive_size += subdirectory.recursive_size

        return self.recursive_size
