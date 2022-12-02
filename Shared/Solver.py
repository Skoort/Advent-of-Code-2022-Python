from abc import ABC, abstractmethod
from enum import Enum


class Part(Enum):
    A = 0
    B = 1

    @staticmethod
    def parse(text):
        text = text.upper()
        if text == 'A':
            return Part.A
        elif text == 'B':
            return Part.B
        else:
            raise Exception(f'Text "{text}" is not a valid Part!')


class Solver(ABC):
    @abstractmethod
    def solve(self, part: Part) -> str:
        pass


if __name__ == '__main__':
    print('Running Solver.py unit tests.')

    assert Part.A.value == 0
    assert Part.B.value == 1
    assert Part.A == Part.A
    assert Part.A != Part.B

    assert len(list(Part)) == 2
    assert all(a == b for a, b in zip(list(Part), [Part.A, Part.B]))

    assert Part.parse('a') == Part.parse('A') == Part.A
    assert Part.parse('b') == Part.parse('B') == Part.B

    threw = False
    try:
        Part.parse('c')
    except:
        threw = True
    if not threw:
        assert False

    threw = False
    try:
        solver = Solver()
    except:
        threw = True
    if not threw:
        assert False

    print('Unit tests successful.')
