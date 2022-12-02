from Shared.Solver import Solver, Part


class Day01Solver(Solver):
    def __init__(self, groups: list[list[int]]):
        self.__groups = groups

    def solve(self, part: Part) -> str:
        sums = list(sum(group) for group in self.__groups)
        sums.sort(reverse=True)
        if part == Part.A:
            return str(sums[0])
        else:
            return str(sum(sums[:3]))
