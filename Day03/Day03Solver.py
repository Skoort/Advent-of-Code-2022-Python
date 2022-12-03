from Shared.Solver import Solver, Part


class Day03Solver(Solver):
    def __init__(self, compartments: list[(set[str], set[str])]):
        self.__compartments = compartments

    def solve(self, part: Part) -> str:
        if part == Part.A:
            return self.__solve_a()
        else:
            return self.__solve_b()

    def __solve_a(self) -> str:
        shared = list(list(c1 & c2) for c1, c2 in self.__compartments)
        return str(sum(sum(Day03Solver.__map_to_priority(item) for item in group) for group in shared))

    def __solve_b(self) -> str:
        uncompartmentalized = list(c1 | c2 for c1, c2 in self.__compartments)
        groups = [uncompartmentalized[i:i+3] for i in range(0, len(uncompartmentalized), 3)]
        badges = [list(e1 & e2 & e3)[0] for e1, e2, e3 in groups]
        return str(sum(Day03Solver.__map_to_priority(badge) for badge in badges))

    @staticmethod
    def __map_to_priority(item: str):
        if ord('a') <= ord(item) <= ord('z'):
            return ord(item) - ord('a') + 1
        else:
            return ord(item) - ord('A') + 27

