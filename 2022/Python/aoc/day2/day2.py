import os.path

from common.base_day import BaseDay


class Day2(BaseDay):
    def _parse_input(self) -> None:
        input_path = os.path.join(self.input_root_folder, "day2")
        with open(file=input_path, mode="r", encoding="utf-8") as input_file:
            self.input = [line.split(" ") for line in input_file.read().splitlines()]

    def run_part1(self) -> int:
        return sum([Day2._calculate_point(match_up[0], match_up[1]) for match_up in self.input])

    def run_part2(self) -> int:
        def calculate_choice(opponent: str, desired_result: str) -> str:
            if desired_result == "X": # Loss
                if opponent == "A":
                    return "Z"
                elif opponent == "B":
                    return "X"
                else:
                    return "Y"
            elif desired_result == "Y": # Draw
                if opponent == "A":
                    return "X"
                elif opponent == "B":
                    return "Y"
                else:
                    return "Z"
            else: # Win
                if opponent == "A":
                    return "Y"
                elif opponent == "B":
                    return "Z"
                else:
                    return "X"

        return sum ([Day2._calculate_point(match_up[0], calculate_choice(match_up[0], match_up[1])) for match_up in self.input])

    @staticmethod
    def _calculate_point(opponent: str, own: str) -> int:
        """
        Calculate the point based on the two choices. Points are awarded for the selection and the result

        Point system:
        - Selection: rock 1, paper 2 and scissors 3 points
        - Result: loss 0, draw 3 and win 6 points

        :param opponent: What the opponent chosen
        :param own: What you have chosen
        :return: Points for the round
        """
        choice_points: int = -1
        match own:
            case "X":
                choice_points = 1
            case "Y":
                choice_points = 2
            case "Z":
                choice_points = 3
        assert choice_points != -1

        round_result_points: int = -1
        if (opponent == "A" and own == "X") or (opponent == "B" and own == "Y") or (opponent == "C" and own == "Z"):
            round_result_points = 3  # Draw
        elif (opponent == "A" and own == "Y") or (opponent == "B" and own == "Z") or (
                opponent == "C" and own == "X"):
            round_result_points = 6  # Win
        else:
            round_result_points = 0  # Loss
        assert round_result_points != -1

        return choice_points + round_result_points