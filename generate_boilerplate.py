import os
import re

from main import __read_day


def __write_file(filepath, content):
    with open(filepath, 'w+') as handle:
        handle.write(content)


def __write_main_file():
    main_lines = ''
    with open('main.py', 'r') as handle:
        main_lines = handle.readlines()

    # Add import (they look like "from Day05.Day05Parser import Day05Parser")
    prev_day_import_line = -1
    prev_day = -1
    prev_day_str = ''
    for i, line in enumerate(main_lines):
        match = re.match(r'.*?import Day(?P<day>\d+)Parser', line)
        if match:
            curr_day = int(match.group('day'))
            if curr_day > prev_day and curr_day <= int(day):
                prev_day = curr_day
                prev_day_str = match.group('day')
                prev_day_import_line = i

    if prev_day != int(day):
        main_lines = main_lines[:prev_day_import_line+1]\
            + [f'from Day{day}.Day{day}Parser import Day{day}Parser\n']\
            + main_lines[prev_day_import_line+1:]

    # Add parser
    prev_line_nr = -1
    for i, line in enumerate(main_lines):
        if line.find(f'return Day{prev_day_str}Parser()') != -1:
            prev_line_nr = i
            break

    spacing_if = main_lines[prev_line_nr - 1][:main_lines[prev_line_nr - 1].find('elif')]
    spacing_return = main_lines[prev_line_nr][:main_lines[prev_line_nr].find('return')]

    if prev_day != int(day):
        main_lines = main_lines[:prev_line_nr+1]\
            + [
                f'{spacing_if}elif day == {int(day)}:\n',
                f'{spacing_return}return Day{day}Parser()\n'
            ]\
            + main_lines[prev_line_nr+1:]

    __write_file('main.py', ''.join(main_lines))


if __name__ == '__main__':
    day = str(__read_day()).rjust(2, "0")

    dirpath = os.path.join(os.getcwd(), f'Day{day}')

    if os.path.exists(dirpath):
        print('The folder already exists!')
    else:
        os.mkdir(dirpath)

        input0_path = os.path.join(dirpath, 'input0')
        input1_path = os.path.join(dirpath, 'input1')
        parser_path = os.path.join(dirpath, f'Day{day}Parser.py')
        solver_path = os.path.join(dirpath, f'Day{day}Solver.py')

        __write_file(input0_path, '')
        __write_file(input1_path, '')
        __write_file(parser_path, f'''\
from Day{day}.Day{day}Solver import Day{day}Solver
from Shared.Parser import Parser


class Day{day}Parser(Parser):
    def get_solver(self, text: str) -> Day{day}Solver:
        return Day{day}Solver()
''')
        __write_file(solver_path, f'''\
from Shared.Solver import Solver, Part


class Day{day}Solver(Solver):
    def __init__(self):
        pass

    def solve(self, part: Part) -> str:
        return 'SOLVER NOT IMPLEMENTED!'
''')

        __write_main_file()
