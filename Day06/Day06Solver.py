from Shared.Solver import Solver, Part


class Day06Solver(Solver):
    def __init__(self, line: str):
        self.__line = line

    def solve(self, part: Part) -> str:
        region_length = 4 if part == Part.A else 14
        for i in range(len(self.__line)):
            substring = self.__line[i:min(i+region_length, len(self.__line))]
            if len(set(substring)) == region_length:
                return str(i+region_length)
