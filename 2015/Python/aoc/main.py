#!/usr/bin/env python3
import importlib
import os.path


def main():
    print("---- Advent of Code 2015 Python solutions")

    for i in range(1, 25):
        if not os.path.exists(os.path.join(os.getcwd(), f"day{i}")):
            continue

        # Dynamically import day subfolders and classes while instantiating them via
        # getattr. Get the results via the classes being callable.
        module = importlib.import_module(f"day{i}.day{i}")
        class_ = getattr(module, f"Day{i}")()
        result = class_()
        print(f"Day {i}: {result}")


if __name__ == "__main__":
    main()
