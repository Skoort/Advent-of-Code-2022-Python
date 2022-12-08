from Day08.Day08Solver import Day08Solver
from Shared.Parser import Parser


class Day08Parser(Parser):
    def get_solver(self, text: str) -> Day08Solver:
        map = []
        for line in text.strip().split('\n'):
            map.append([])
            for c in line:
                map[-1].append(int(c))
        return Day08Solver(map, (len(map[0]), len(map)))
