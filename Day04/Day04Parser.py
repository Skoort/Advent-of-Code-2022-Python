from Day04.Day04Solver import Day04Solver
from Shared.Parser import Parser


class Day04Parser(Parser):
    def get_solver(self, text: str) -> Day04Solver:
        pairs = []
        lines = text.strip().split('\n')
        for line in lines:
            pair = tuple(tuple(int(y) for y in x.split('-')) for x in line.split(','))
            pairs.append(pair)
        return Day04Solver(pairs)
