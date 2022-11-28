from dataclasses import dataclass


@dataclass
class BoxDimension:
    length: int
    width: int
    height: int

    def get_wrapping_paper_length(self) -> int:
        length_width = self.length * self.width
        width_height = self.width * self.height
        height_length = self.height * self.length
        smallest_side = min(length_width, width_height, height_length)
        total_surface_area = 2 * length_width + 2 * width_height + 2 * height_length + smallest_side

        return total_surface_area

    def get_ribbon_length(self) -> int:
        smallest_two_sides = sorted([self.length, self.width, self.height])[:2]
        ribbon_length = 2 * smallest_two_sides[0] + 2 * smallest_two_sides[1]
        bow = self.length * self.width * self.height

        return ribbon_length + bow
