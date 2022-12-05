import copy

from Shared.Solver import Solver, Part


class Day05Solver(Solver):
    def __init__(self, columns: list[list[str]], instructions: list[(int, int, int)]):
        self.__columns = columns
        self.__instructions = instructions

    def solve(self, part: Part) -> str:
        working_columns = copy.deepcopy(self.__columns)
        for instruction in self.__instructions:
            amount = instruction[0]
            from_index = instruction[1] - 1
            to_index = instruction[2] - 1

            if part == Part.A:
                for i in range(amount):
                    cargo = working_columns[from_index].pop()
                    working_columns[to_index].append(cargo)
            else:
                from_column = working_columns[from_index]
                to_column = working_columns[to_index]
                working_columns[from_index] = from_column[:-amount]
                working_columns[to_index] = [*to_column, *from_column[-amount:]]

        return ''.join(column[-1] for column in working_columns)
