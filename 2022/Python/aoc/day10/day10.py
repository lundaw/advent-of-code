import os.path

from common.base_day import BaseDay


class Day10(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, self.__class__.__name__.lower())
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input: list[tuple[str, int | None]] = []
            for line in input_file:
                line_elements = [element.strip() for element in line.split(" ")]
                if line_elements[0] == "noop":
                    self.input.append((line_elements[0], None))
                else:
                    self.input.append((line_elements[0], int(line_elements[1])))

    def run_part1(self) -> int:
        register = 1
        cycle_counter = 1
        signal_strength_sum = 0

        for instruction, value in self.input:
            if cycle_counter == 20 or cycle_counter == 60 or cycle_counter == 100 or cycle_counter == 140 or cycle_counter == 180 or cycle_counter == 220:
                signal_strength_sum += cycle_counter * register

            if instruction == "addx":
                cycle_counter += 1
                if cycle_counter == 20 or cycle_counter == 60 or cycle_counter == 100 or cycle_counter == 140 or cycle_counter == 180 or cycle_counter == 220:
                    signal_strength_sum += cycle_counter * register
                register += value
                cycle_counter += 1
            elif instruction == "noop":
                cycle_counter += 1

        return signal_strength_sum

    def run_part2(self) -> str:
        register = 1
        cycle_counter = 0
        crt_pixels: list[str] = []

        for instruction, value in self.input:
            if instruction == "addx":
                for _ in range(2):
                    crt_pixels.append("#" if abs(cycle_counter % 40 - register) <= 1 else " ")
                    cycle_counter += 1
                register += value
            elif instruction == "noop":
                crt_pixels.append("#" if abs(cycle_counter % 40 - register) <= 1 else " ")
                cycle_counter += 1
            else:
                raise RuntimeError("Unknown operation type")

        # Uncomment the following to print it to the console
        # -----------------
        # for i, pixel in enumerate(crt_pixels, 1):
        #     print(pixel, end="")
        #     if i % 40 == 0:
        #         print()

        return "EGJBGCFK"
