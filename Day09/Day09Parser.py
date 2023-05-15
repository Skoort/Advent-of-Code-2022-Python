from Day09.Day09Solver import Day09Solver
from Shared.Parser import Parser


class Day09Parser(Parser):
    def get_solver(self, text: str) -> Day09Solver:
        instructions = []
        for line in text.strip().split('\n'):
            dir, amount = line.split()
            instructions.append((dir, int(amount)))
        return Day09Solver(instructions)
