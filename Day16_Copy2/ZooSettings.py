from typing import Tuple


class ZooSettings:
    def __init__(self, valves: dict[int, Tuple[int, list[int]]], name_to_index: dict[str, int], index_to_name: dict[int, str], start_valve_index: int):
        # Individual settings
        self.time_limit = 30
        self.name_to_index = name_to_index
        self.index_to_name = index_to_name
        self.valves = valves
        self.num_valves = len(self.index_to_name.keys())
        self.start_valve_index = start_valve_index
        # This way there is usually at least 5 mutations per offspring.
        self.mutation_chance = 1.0 / (self.time_limit / 3.0)

        # Zoo settings
        self.population_size = 100
        self.keep_amount = 10
        self.new_amount = 20
        self.tournament_size = 5
