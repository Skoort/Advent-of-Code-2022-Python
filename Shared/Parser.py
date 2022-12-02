from abc import ABC, abstractmethod

from Shared.Solver import Solver


class Parser(ABC):
    @abstractmethod
    def get_solver(self, text: str) -> Solver:
        pass


if __name__ == '__main__':
    print('Running Parser.py unit tests.')

    threw = False
    try:
        parser = Parser()
    except:
        threw = True
    if not threw:
        assert False

    print('Unit tests successful.')
