from Shared.Solver import Solver, Part


class Day09Solver(Solver):
    def __init__(self, instructions: list[(str, int)]):
        self.__instructions = instructions
        self.__knots = []
        self.__tail_positions = []

    def solve(self, part: Part) -> str:
        self.__reset(part)
        for dir, amount in self.__instructions:
            for move in range(amount):
                self.__move_head(dir)
                for i in reversed(range(len(self.__knots) - 1)):
                    self.__move_tail(i)
                self.__add_tail_position()
        return str(len(self.__tail_positions))

    def __reset(self, part: Part) -> None:
        if part == Part.A:
            n = 2
        else:
            n = 10
        self.__knots = list((0, 0) for _ in range(n))
        self.__tail_positions = [(0, 0)]

    def __move_head(self, dir: str) -> None:
        head = self.__knots[-1]
        if dir == 'U':
            head = (head[0], head[1] + 1)
        elif dir == 'R':
            head = (head[0] + 1, head[1])
        elif dir == 'D':
            head = (head[0], head[1] - 1)
        elif dir == 'L':
            head = (head[0] - 1, head[1])
        self.__knots[-1] = head

    def __move_tail(self, index: int) -> None:
        tail = self.__knots[index]
        head = self.__knots[index + 1]

        if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) <= 1:
            # Within one unit
            return

        tail = (
            tail[0] + max(-1, min(1, head[0] - tail[0])),
            tail[1] + max(-1, min(1, head[1] - tail[1]))
        )
        self.__knots[index] = tail

    def __add_tail_position(self) -> None:
        tail = self.__knots[0]
        for x, y in self.__tail_positions:
            if x == tail[0] and y == tail[1]:
                return
        self.__tail_positions.append(tail)
