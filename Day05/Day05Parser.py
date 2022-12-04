from Day05.Day05Solver import Day05Solver
from Shared.Parser import Parser


class Day05Parser(Parser):
    def get_solver(self, text: str) -> Day05Solver:
        return Day05Solver()
