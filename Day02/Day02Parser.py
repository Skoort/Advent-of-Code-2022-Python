from Day02.Choice import Choice
from Day02.Day02Solver import Day02Solver
from Shared.Parser import Parser


class Day02Parser(Parser):
    def get_solver(self, text: str) -> Day02Solver:
        choices = list(tuple(Choice.parse(choice) for choice in line.split()) for line in text.split('\n'))
        return Day02Solver(choices)
