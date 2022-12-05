from Shared.Solver import Solver, Part


class Day05Solver(Solver):
    def __init__(self, columns, instructions):
        self.__columns = columns
        self.__instructions = instructions

    def solve(self, part: Part) -> str:
        for instruction in self.__instructions:
            amount = instruction[0]
            from_index = instruction[1] - 1
            to_index = instruction[2] - 1

            if part == Part.A:
                for i in range(amount):
                    cargo = self.__columns[from_index].pop()
                    self.__columns[to_index].append(cargo)
            else:
                from_column = self.__columns[from_index]
                to_column = self.__columns[to_index]
                self.__columns[from_index] = from_column[:-amount]
                self.__columns[to_index] = [*to_column, *from_column[-amount:]]

        return ''.join(column[-1] for column in self.__columns)
