import copy
import os.path
import re

from common.base_day import BaseDay
from day5.move import Move


class Day5(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day5")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            raw_input = input_file.read()

        self.stacks: list[list[str]] = []
        stack_start: list[str]
        moves: list[str]
        stack_start, moves = list(map(lambda p: p.splitlines(), raw_input.split("\n\n")))
        for _ in re.findall(r"(\d+)", stack_start[-1]):
            self.stacks.append([])
        stack_start_extractor_regex = re.compile(r"(\[[a-zA-Z]] ?| {4})")
        for row in stack_start[:-1]:
            for i, group in enumerate(stack_start_extractor_regex.findall(row)):
                if not group.isspace():
                    self.stacks[i].append(group[1])
        for stack in self.stacks:
            stack.reverse()

        self.moves: list[Move] = []
        move_extractor_regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
        for move in moves:
            amount, from_, to = move_extractor_regex.match(move).groups()
            self.moves.append(Move(amount=int(amount), from_=int(from_) - 1, to=int(to) - 1))

    def run_part1(self) -> str:
        stacks_copy = copy.deepcopy(self.stacks)
        for move in self.moves:
            for _ in range(move.amount):
                stacks_copy[move.to].append(stacks_copy[move.from_].pop())

        return "".join([stack[-1] for stack in stacks_copy])

    def run_part2(self) -> str:
        stacks_copy = copy.deepcopy(self.stacks)
        for move in self.moves:
            stacks_copy[move.to] += stacks_copy[move.from_][-move.amount:]
            stacks_copy[move.from_] = stacks_copy[move.from_][:-move.amount]

        return "".join([stack[-1] for stack in stacks_copy])
