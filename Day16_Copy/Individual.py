from random import randrange, random
from typing import Tuple

from Day16.ZooSettings import ZooSettings


class Individual:
    # For internal use only. Use the Individual.random or Individual.breed methods to create new Individuals!!!
    def __init__(self, settings: ZooSettings, representation: list[str]):
        self.__settings = settings
        self.__representation = representation
        self.__cached_fitness = -1
        self.__cached_is_invalid = True

    def evaluate_fitness(self):
        if self.__cached_fitness != -1:
            return self.__cached_fitness

        minute = 0
        opened_valves = []
        # The pressure released by this individual before its first mistake.
        released_pressure = 0

        bonus_points = 0

        is_invalid = False
        prev_valve = None
        for i, valve_name in enumerate(self.__representation):
            # The valves release pressure at the start of each minute.
            for valve in opened_valves:
                released_pressure = released_pressure + valve[0]

            valve_index = self.__settings.name_to_index[valve_name]
            valve = self.__settings.valves[valve_index]

            if i == 0 and valve_index != self.__settings.start_valve_index:
                # The individual started at the wrong valve.
                is_invalid = True
                break

            if prev_valve is not None:
                if prev_valve == valve:
                    # We assume that an individual opens a valve if it stays by it for longer than a minute.
                    if valve in opened_valves:
                        # Standing at the same place longer than necessary is a waste.
                        bonus_points = bonus_points - 1
                    else:
                        opened_valves.append(valve)
                elif valve_index not in prev_valve[1]:
                    # The individual made an invalid move.
                    is_invalid = True
                    break

            # Reward for this move not being invalid.
            bonus_points = bonus_points + 1

            minute = minute + 1
            prev_valve = valve

        self.__cached_is_invalid = is_invalid
        self.__cached_fitness = released_pressure + bonus_points * 0.01
        return self.__cached_fitness

    def __repr__(self):
        return '->'.join(self.__representation)

    @staticmethod
    def random(settings: ZooSettings) -> 'Individual':
        representation = [
            settings.index_to_name[randrange(settings.num_valves)]
            for _ in range(settings.time_limit)
        ]
        individual = Individual(settings, representation)
        return individual

    @staticmethod
    def breed(parent1: 'Individual', parent2: 'Individual') -> Tuple['Individual', 'Individual']:
        return Individual.__uniform_crossover(parent1, parent2)

    @staticmethod
    def __one_point_crossover(parent1: 'Individual', parent2: 'Individual') -> Tuple['Individual', 'Individual']:
        settings = parent1.__settings
        crossover_point = randrange(settings.time_limit)
        offspring1 = Individual(settings, [
            Individual.try_mutate(settings, parent1.__representation[i] if i <= crossover_point else parent2.__representation[i])
            for i in range(settings.time_limit)
        ])
        offspring2 = Individual(settings, [
            Individual.try_mutate(settings, parent2.__representation[i] if i <= crossover_point else parent1.__representation[i])
            for i in range(settings.time_limit)
        ])
        return offspring1, offspring2

    @staticmethod
    def __uniform_crossover(parent1: 'Individual', parent2: 'Individual') -> Tuple['Individual', 'Individual']:
        settings = parent1.__settings
        offspring1 = Individual(settings, [
            Individual.try_mutate(settings, parent1.__representation[i] if random() < 0.5 else parent2.__representation[i])
            for i in range(settings.time_limit)
        ])
        offspring2 = Individual(settings, [
            Individual.try_mutate(settings, parent1.__representation[i] if random() < 0.5 else parent2.__representation[i])
            for i in range(settings.time_limit)
        ])
        return offspring1, offspring2

    @staticmethod
    def try_mutate(settings: ZooSettings, input_value: str) -> str:
        if random() < settings.mutation_chance:
            return settings.index_to_name[randrange(settings.num_valves)]
        else:
            return input_value
