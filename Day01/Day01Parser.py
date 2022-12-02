from Day01.Day01Solver import Day01Solver
from Shared.Parser import Parser


class Day01Parser(Parser):
    def get_solver(self, text: str) -> Day01Solver:
        elves = []
        elf = None

        lines = text.strip().split('\n')
        for line in lines:
            if line == '' or line.isspace():
                elf = None
                continue

            if elf is None:
                elf = []
                elves.append(elf)

            elf.append(int(line))

        return Day01Solver(elves)
