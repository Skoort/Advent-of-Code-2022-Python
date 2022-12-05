from Day05.Day05Solver import Day05Solver
from Shared.Parser import Parser


class Day05Parser(Parser):
    def get_solver(self, text: str) -> Day05Solver:
        index = text.find('move')
        text1 = text[:index]
        text2 = text[index:]

        lines1 = text1.rstrip().split('\n')
        lines1.reverse()

        column_indices = [i for i, c in enumerate(lines1[0]) if c.isnumeric()]
        columns = [[] for _ in range(len(column_indices))]
        lines1 = lines1[1:]

        for line in lines1:
            filled_columns = [(i, c) for i, c in enumerate(line) if c.isalpha()]
            for i, c in filled_columns:
                column_index = column_indices.index(i)
                columns[column_index].append(c)

        text2 = text2.replace('move', '').replace('from', '').replace('to', '')

        instructions = []

        for line in text2.strip().split('\n'):
            instructions.append(tuple(int(word) for word in line.strip().split()))

        return Day05Solver(columns, instructions)
