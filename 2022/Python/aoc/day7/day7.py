import os.path

from common.base_day import BaseDay
from day7.directory_entry import DirectoryEntry


class Day7(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, self.__class__.__name__.lower())
        self.root_directory: DirectoryEntry = DirectoryEntry(name="/")
        self.all_directories: list[DirectoryEntry] = []
        current_directory: DirectoryEntry = self.root_directory

        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            for row in input_file.read().splitlines()[1:]:
                elements = row.split(" ")
                if row.startswith("$"):
                    if elements[1] == "cd":
                        if elements[2] == "..":
                            current_directory = current_directory.parent
                        else:
                            current_directory = current_directory.subdirectories[elements[2]]
                else:
                    if elements[0] == "dir":
                        folder_name = elements[1]
                        new_directory_entry = DirectoryEntry(name=folder_name, parent=current_directory)
                        self.all_directories.append(new_directory_entry)
                        current_directory.subdirectories[folder_name] = new_directory_entry
                    else:
                        current_directory.size += int(elements[0])

        self.root_directory.calculate_recursive_size()

    def run_part1(self) -> int:
        max_directory_size = 100_000
        return sum(
            map(
                lambda d: d.recursive_size,
                filter(lambda d: d.recursive_size <= max_directory_size, self.all_directories)
            )
        )

    def run_part2(self) -> int:
        total_disk_space = 70_000_000
        minimum_free_space = 30_000_000
        current_free_space = total_disk_space - self.root_directory.recursive_size
        space_to_free = minimum_free_space - current_free_space

        return min(
            map(
                lambda d: d.recursive_size,
                filter(lambda d: d.recursive_size >= space_to_free, self.all_directories)
            )
        )
