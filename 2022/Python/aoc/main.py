#!/usr/bin/env python3
import importlib
import os.path


def run_day(day: int) -> None:
    module = importlib.import_module(f"day{day}.day{day}")
    class_ = getattr(module, f"Day{day}")()
    result = class_()
    print(f"Day {day}: {result}")


def main():
    print("---- Advent of Code 2022 Python solutions")

    for i in range(1, 25):
        if not os.path.exists(os.path.join(os.getcwd(), f"day{i}")):
            continue

        # Dynamically import day subfolders and classes while instantiating them via
        # getattr. Get the results via the classes being callable.
        run_day(i)


if __name__ == "__main__":
    main()
