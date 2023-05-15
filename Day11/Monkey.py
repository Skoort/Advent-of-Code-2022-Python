import typing
from collections import deque


class Monkey:
    def __init__(self, id: int, starting_items: tuple[int], operator: str, arg1: str, arg2: str, divisible_by: int, throw_to_0: int, throw_to_1: int):
        self.id = id
        self.starting_items = starting_items
        self.__operator = operator;
        self.__arg1 = arg1;
        self.__arg2 = arg2;
        self.divisible_by = divisible_by;
        self.__throw_to_0 = throw_to_0;
        self.__throw_to_1 = throw_to_1;

        self.items = deque(self.starting_items)
        self.num_throws = 0

    def inspect_operation(self, value):
        x = value if self.__arg1 == 'old' else int(self.__arg1)
        y = value if self.__arg2 == 'old' else int(self.__arg2)
        if self.__operator == '+':
            return x + y
        elif self.__operator == '-':
            return x - y
        elif self.__operator == '*':
            return x * y
        else:
            raise Exception('That operator is not supported!')

    def throw_operation(self, value):
        if value % self.divisible_by == 0:
            return self.__throw_to_0
        else:
            return self.__throw_to_1
