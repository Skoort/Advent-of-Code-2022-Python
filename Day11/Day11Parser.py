import typing

from Day11.Day11Solver import Day11Solver
from Day11.Monkey import Monkey
from Shared.Parser import Parser


class Day11Parser(Parser):
    def get_solver(self, text: str) -> Day11Solver:
        monkeys = []
        lines = text.strip().split('\n')
        i = 0
        monkey_index = 0
        while i < len(lines):
            starting_items = list(int(x) for x in lines[i+1].replace('Starting items:', '').strip().split(','))
            operation_text = ''.join(x for x in lines[i+2].replace('Operation: new = ', '')).strip()
            arg1, operator, arg2 = operation_text.split()
            # inspect_operation = Day11Parser.__create_operation(operator, arg1, arg2)
            divisible_by = int(lines[i+3].replace('Test: divisible by', '').strip())
            monkey_if_true = int(lines[i+4].replace('If true: throw to monkey', '').strip())
            monkey_if_false = int(lines[i+5].replace('If false: throw to monkey', '').strip())
            # throw_operation = lambda v, d=divisible_by, m1=monkey_if_true, m2=monkey_if_false: m1 if v % d == 0 else m2

            # monkeys.append(Monkey(monkey_index, starting_items, inspect_operation, throw_operation))
            monkeys.append(Monkey(monkey_index, starting_items, operator, arg1, arg2, divisible_by, monkey_if_true, monkey_if_false))

            i = i + 7  # Also skip the blank line between monkeys.
            monkey_index = monkey_index + 1

        return Day11Solver(monkeys)

    # @staticmethod
    # def __create_operation(operator: str, arg1: str, arg2: str) -> typing.Callable[[int], int]:
    #     parse_arg = lambda value, arg: value if arg == 'old' else int(arg)
    #     if operator == '+':
    #         return lambda v: parse_arg(v, arg1) + parse_arg(v, arg2)
    #     elif operator == '-':
    #         return lambda v: parse_arg(v, arg1) - parse_arg(v, arg2)
    #     elif operator == '*':
    #         return lambda v: parse_arg(v, arg1) * parse_arg(v, arg2)
    #     else:
    #         raise Exception('That operator is not supported!')
