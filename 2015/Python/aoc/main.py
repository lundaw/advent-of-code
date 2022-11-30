#!/usr/bin/env python3
import importlib
import os.path
from concurrent.futures import ThreadPoolExecutor


def run_day(day: int) -> None:
    """
    Dynamically import day folders and classes while instantiating them via
    getattr. Get the results via the classes being callable.

    :param day: Number of day to import and run between 1 and 25, inclusive.
    :return:
    """

    if day < 0 or day > 25:
        raise RuntimeError(f"Day {day} is out of range for running")

    module = importlib.import_module(f"day{day}.day{day}")
    class_ = getattr(module, f"Day{day}")()
    result = class_()

    return result


def main():
    print("---- Advent of Code 2015 Python solutions")

    results: dict[int, tuple[int, int]] = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(1, 25):
            if not os.path.exists(os.path.join(os.getcwd(), f"day{i}")):
                continue

            task = executor.submit(run_day, i)
            results[i] = task.result()

    for day, (part1, part2) in results.items():
        print(f"Day {day}: ({part1}, {part2})")


if __name__ == "__main__":
    main()
