import copy
from collections import deque
from math import floor

from Day11.Monkey import Monkey
from Shared.Solver import Solver, Part


class Day11Solver(Solver):
    def __init__(self, monkeys: list[Monkey]):
        self.__monkeys = monkeys

    def solve(self, part: Part) -> str:
        for monkey in self.__monkeys:
            monkey.items = deque(monkey.starting_items)
            monkey.num_throws = 0

        n = 20 if part == Part.A else 10000
        total_divisibility = 1
        for divisible_by in set(monkey.divisible_by for monkey in self.__monkeys):
            total_divisibility = total_divisibility * divisible_by

        for round in range(n):
            if round % 50 == 0:
                print(f"Round {round}")
            for monkey_from in self.__monkeys:
                while len(monkey_from.items) > 0:
                    item_value = monkey_from.items[0]



                    if part == Part.A:
                        new_item_value = floor(monkey_from.inspect_operation(item_value) / 3.0)
                    else:
                        new_item_value = monkey_from.inspect_operation(item_value) % total_divisibility
                    monkey_to = self.__monkeys[monkey_from.throw_operation(new_item_value)]
                    monkey_from.items.popleft()
                    monkey_to.items.append(new_item_value)
                    monkey_from.num_throws = monkey_from.num_throws + 1
        top_num_throws = list(map(lambda monkey: monkey.num_throws, self.__monkeys))
        top_num_throws.sort(reverse=True)
        return str(top_num_throws[0] * top_num_throws[1])

