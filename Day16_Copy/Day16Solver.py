from random import randrange, random

from Day16.Individual import Individual
from Day16.ZooSettings import ZooSettings
from Shared.Solver import Solver, Part


class Day16Solver(Solver):
    def __init__(self, settings: ZooSettings):
        self.__settings = settings
        self.__individuals = []
        self.__generation_num = 1
        self.__should_print = False
        self.__seen_individuals = set()

    def solve(self, part: Part) -> str:
        good_starting_points = []
        for i in range(self.__settings.population_size):
            print(f'Running short simulation to find good starting points. {i+1}/{self.__settings.population_size}')
            self.__reset()
            self.__run(300)
            self.__print_best_individual()
            good_starting_points.append(self.__individuals[0])
        print('Running long simulation using good starting points.')
        self.__individuals = good_starting_points
        self.__individuals.sort(reverse=True, key=lambda individual: individual.evaluate_fitness())
        self.__seen_individuals = set(repr(individual) for individual in self.__individuals)
        self.__generation_num = 2
        self.__should_print = True
        self.__run(100000, True)

        return self.__individuals[0].evaluate_fitness()

    def __reset(self) -> None:
        self.__individuals = []
        self.__generation_num = 1
        self.__should_print = False

    def __run(self, max_iters: int, should_print: bool = False) -> None:
        while self.__generation_num <= max_iters:
            if should_print and (self.__generation_num == 1 or (self.__generation_num % 1000) == 0):
                print(f'Generation {self.__generation_num}')
            self.__generate_new_generation(should_print)
            self.__generation_num = self.__generation_num + 1

    def __generate_new_generation(self, should_print: bool) -> None:
        if self.__generation_num == 1:
            self.__individuals = [Individual.random(self.__settings) for _ in range(self.__settings.population_size)]
            self.__seen_individuals = set(repr(individual) for individual in self.__individuals)
        else:
            keep_amount = self.__settings.keep_amount
            new_amount = self.__settings.new_amount
            breed_amount = self.__settings.population_size - keep_amount - new_amount

            new_generation = []
            for i in range(keep_amount):
                new_generation.append(self.__individuals[i])

            for _ in range(new_amount):
                new_generation.append(Individual.random(self.__settings))

            while len(new_generation) < self.__settings.population_size:
                parent1 = self.__hold_tournament()
                parent2 = self.__hold_tournament(parent1)
                child1, child2 = Individual.breed(parent1, parent2)
                if child1 not in self.__seen_individuals or random() < 0.25:
                    new_generation.append(child1)
                self.__seen_individuals.add(repr(child1))
                if child2 not in self.__seen_individuals or random() < 0.25:
                    new_generation.append(child1)
                self.__seen_individuals.add(repr(child2))
                new_generation.extend(Individual.breed(parent1, parent2))

            self.__individuals = new_generation

        self.__individuals.sort(reverse=True, key=lambda individual: individual.evaluate_fitness())

        if should_print and (self.__generation_num == 1 or (self.__generation_num % 1000) == 0):
            self.__print_best_individual()

    def __print_best_individual(self):
        best_individual = self.__individuals[0]
        print(f'Best individual: {best_individual}')
        print(f'Fitness: {best_individual.evaluate_fitness()}')
        print(f'Released pressure: {int(best_individual.evaluate_fitness())}')

    def __hold_tournament(self, other_parent: Individual = None) -> Individual:
        best_fitness = -1
        best_individual = None
        chosen_individuals = []
        while len(chosen_individuals) < self.__settings.tournament_size:
            random_index = randrange(len(self.__individuals))
            individual = self.__individuals[random_index]
            if individual != other_parent and individual not in chosen_individuals:
                chosen_individuals.append(individual)
                fitness = individual.evaluate_fitness()
                if fitness > best_fitness:
                    best_individual = individual
                    best_fitness = fitness
        return best_individual
