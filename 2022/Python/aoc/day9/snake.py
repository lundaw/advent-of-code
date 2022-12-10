from day9.position import Position


class Snake:
    def __init__(self, length: int = 1):
        self.parts: list[tuple[Position, Position]] = []
        head: Position = Position(0, 0)
        tail: Position = Position(0, 0)
        for i in range(0, length, 1):
            self.parts.append((head, tail))
            head = tail
            tail = Position(0, 0)

    def step(self, direction: str, amount: int):
        tail_visited_positions: set[tuple[int, int]] = set()

        for _ in range(0, amount):
            head, tail = self.parts[0]
            self._move_position(head, direction)

            for pair_head, pair_tail in self.parts:
                if pair_head.x == pair_tail.x and pair_head.y == pair_tail.y:
                    break

                self._move_tail_closer(pair_head, pair_tail)

            last_head, last_tail = self.parts[-1]
            if len(self.parts) == 1:
                tail_visited_positions.add((last_tail.x, last_tail.y))
            else:
                tail_visited_positions.add((last_head.x, last_head.y))
        return tail_visited_positions

    @staticmethod
    def _move_position(position: Position, direction: str):
        match direction:
            case "R":
                position.x += 1
            case "L":
                position.x -= 1
            case "U":
                position.y += 1
            case "D":
                position.y -= 1

    @staticmethod
    def _move_tail_closer(head: Position, tail: Position):
        # Tail is too far away from head, move it closer
        if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
            # Head and tail is in the same row
            if head.x == tail.x:
                if head.y > tail.y:
                    tail.y += 1
                else:
                    tail.y -= 1
            # Head and tail is in the same column
            elif head.y == tail.y:
                if head.x > tail.x:
                    tail.x += 1
                else:
                    tail.x -= 1
            else:
                # Head is right and up
                if head.x > tail.x and head.y > tail.y:
                    tail.x += 1
                    tail.y += 1
                # Head is right and down
                elif head.x > tail.x and head.y < tail.y:
                    tail.x += 1
                    tail.y -= 1
                # Head is left and up
                elif head.x < tail.x and head.y > tail.y:
                    tail.x -= 1
                    tail.y += 1
                # Head is left and down
                elif head.x < tail.x and head.y < tail.y:
                    tail.x -= 1
                    tail.y -= 1
                # Shouldn't be possible
                else:
                    raise RuntimeError("HUH")