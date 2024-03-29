import os
import sys

# -- This code is auto generated. Do not touch. -------
from Day01.Day01Parser import Day01Parser
from Day02.Day02Parser import Day02Parser
from Day03.Day03Parser import Day03Parser
from Day04.Day04Parser import Day04Parser
from Day05.Day05Parser import Day05Parser
from Day06.Day06Parser import Day06Parser
from Day07.Day07Parser import Day07Parser
from Day08.Day08Parser import Day08Parser
from Day09.Day09Parser import Day09Parser
from Day10.Day10Parser import Day10Parser
from Day11.Day11Parser import Day11Parser
from Day12.Day12Parser import Day12Parser
from Day14.Day14Parser import Day14Parser
from Day15.Day15Parser import Day15Parser
from Day16.Day16Parser import Day16Parser
# -----------------------------------------------------

from Shared.Parser import Parser
from Shared.Solver import Part


def __parse_day(text: str) -> int:
    try:
        day = int(text)
        if 1 <= day <= 25:
            return day
    except:
        pass

    raise Exception('Day is invalid!')


def __parse_part(text: str) -> Part:
    try:
        return Part.parse(text)
    except:
        raise Exception('Part is invalid!')


def __parse_file(filepath: str) -> str:
    if filepath == '0' or filepath == '1':
        filepath = f'input{filepath}'

    filepath = os.path.join(f"Day{str(day).rjust(2, '0')}", filepath)

    with open(filepath, 'r') as handle:
        return handle.read()


def __read_day() -> int:
    while True:
        try:
            return __parse_day(input('Enter a day (1-25): '))
        except Exception as e:
            print(str(e))


def __read_part() -> Part:
    while True:
        try:
            return __parse_part(input('Enter a part (A or B): '))
        except Exception as e:
            print(str(e))


def __read_file() -> str:
    while True:
        try:
            return __parse_file(input('Enter a file: '))
        except:
            print('Failed to read file!')


def __get_parser(day: int) -> Parser:
    # -- This code is auto generated. Do not touch. ------
    if day == 1:
        return Day01Parser()
    elif day == 2:
        return Day02Parser()
    elif day == 3:
        return Day03Parser()
    elif day == 4:
        return Day04Parser()
    elif day == 5:
        return Day05Parser()
    elif day == 6:
        return Day06Parser()
    elif day == 7:
        return Day07Parser()
    elif day == 8:
        return Day08Parser()
    elif day == 9:
        return Day09Parser()
    elif day == 10:
        return Day10Parser()
    elif day == 11:
        return Day11Parser()
    elif day == 12:
        return Day12Parser()
    elif day == 14:
        return Day14Parser()
    elif day == 15:
        return Day15Parser()
    elif day == 16:
        return Day16Parser()
    else:
        raise NotImplementedError('That day is not yet implemented!')
    # ---------------------------------------------------


if __name__ == '__main__':
    try:
        day = __parse_day(sys.argv[1]) if len(sys.argv) >= 2 else __read_day()
        part = __parse_part(sys.argv[2]) if len(sys.argv) >= 3 else __read_part()
        text = __parse_file(sys.argv[3]) if len(sys.argv) >= 4 else __read_file()

        parser = __get_parser(day)
        solver = parser.get_solver(text)

        print(solver.solve(part))
    except Exception as e:
        print(str(e))
