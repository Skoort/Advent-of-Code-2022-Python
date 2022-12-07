from Day06.Day06Solver import Day06Solver
from Shared.Parser import Parser


class Day06Parser(Parser):
    def get_solver(self, text: str) -> Day06Solver:
        return Day06Solver(text)
