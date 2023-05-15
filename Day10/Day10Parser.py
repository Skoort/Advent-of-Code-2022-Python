from Day10.Day10Solver import Day10Solver
from Shared.Parser import Parser


class Day10Parser(Parser):
    def get_solver(self, text: str) -> Day10Solver:
        instructions = []
        for line in text.strip().split('\n'):
            words = line.split()
            command = words[0]
            arguments = tuple(words[1:])
            instructions.append((command, arguments))
        return Day10Solver(instructions)
