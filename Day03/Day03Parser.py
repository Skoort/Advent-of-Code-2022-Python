from Day03.Day03Solver import Day03Solver
from Shared.Parser import Parser


class Day03Parser(Parser):
    def get_solver(self, text: str) -> Day03Solver:
        compartments = []
        for line in text.strip().split('\n'):
            compartment_size = int(len(line) / 2)
            c1 = set(line[:compartment_size])
            c2 = set(line[compartment_size:])
            compartments.append((c1, c2))
        return Day03Solver(compartments)
