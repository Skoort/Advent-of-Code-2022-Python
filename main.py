import os
import sys

from Day01.Day01Parser import Day01Parser
from Day02.Day02Parser import Day02Parser
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
    if day == 1:
        return Day01Parser()
    elif day == 2:
        return Day02Parser()
    else:
        raise NotImplementedError('That day is not yet implemented!')


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
