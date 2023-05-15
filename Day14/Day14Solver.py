from collections import deque

from Day14.Sand import Sand
from Day14.Tile import Tile, TileType
from Shared.Solver import Solver, Part


class Day14Solver(Solver):
    def __init__(self, min_point: (int, int), max_point: (int, int), dimensions: (int, int), map: list[list[Tile]], sand_spawn: (int, int)):
        self.__min_point = min_point
        self.__max_point = max_point
        self.__dimensions = dimensions
        self.__map = map
        self.__sand_spawn = sand_spawn
        self.__sand = []
        self.__settled = []

    def __to_local(self, position):
        return position[0] - self.__min_point[0], position[1] - self.__min_point[1]

    def __to_global(self, position):
        return position[0] + self.__min_point[0], position[1] + self.__min_point[1]

    def __try_to_move(self, sand: Sand, from_local: (int, int), to_local: (int, int)) -> bool:
        tile_from = self.__map[from_local[1]][from_local[0]]
        tile_to = self.__map[to_local[1]][to_local[0]]
        if not tile_to.is_occupied:
            sand.position = (tile_to.x, tile_to.y)
            tile_from.is_occupied = False
            tile_to.is_occupied = True
            tile_to.visit_count = tile_to.visit_count + 1
            return True
        else:
            return False

    def __prepare_part_b(self):
        max_depth = abs(self.__sand_spawn[1] - self.__max_point[1]) + 2
        self.__old_min_point = self.__min_point
        self.__min_point = (min(self.__min_point[0], self.__sand_spawn[0] - max_depth), self.__min_point[1])
        self.__old_max_point = self.__max_point
        self.__max_point = (max(self.__max_point[0], self.__sand_spawn[0] + max_depth), self.__max_point[1] + 2)
        self.__old_dimensions = self.__dimensions
        self.__dimensions = (self.__max_point[0] - self.__min_point[0] + 1, self.__max_point[1] - self.__min_point[1] + 1)
        self.__old_map = self.__map
        self.__map = [[Tile(x + self.__min_point[0], y + self.__min_point[1], TileType.ROCK if y == (self.__dimensions[1] - 1) else TileType.AIR) for x in range(self.__dimensions[0])] for y in range(self.__dimensions[1])];

        for x in range(self.__old_dimensions[0]):
            for y in range(self.__old_dimensions[1]):
                old_tile = self.__old_map[y][x]
                local_x, local_y = self.__to_local((old_tile.x, old_tile.y))
                new_tile = self.__map[local_y][local_x]
                new_tile.type = old_tile.type
                new_tile.is_occupied = old_tile.is_occupied

    def solve(self, part: Part) -> str:
        if part == Part.B:
            self.__prepare_part_b()

        is_out_of_bounds = False

        spawn_x_local, spawn_y_local = self.__to_local(self.__sand_spawn)
        spawn_tile = self.__map[spawn_y_local][spawn_x_local]

        i = 0
        while True:
            if (i % 100 == 0) or is_out_of_bounds or spawn_tile.is_occupied:
                self.__print()

            if is_out_of_bounds:
                break

            if spawn_tile.is_occupied:
                break

            self.__sand.append(Sand(self.__sand_spawn))

            sand_settled = []

            for sand in self.__sand:
                local_x, local_y = self.__to_local(sand.position)

                if local_y + 1 < self.__dimensions[1]:
                    if self.__try_to_move(sand, (local_x, local_y), (local_x, local_y + 1)):
                        continue
                else:
                    is_out_of_bounds = True
                    break

                if not is_out_of_bounds and local_x - 1 >= 0:
                    if self.__try_to_move(sand, (local_x, local_y), (local_x - 1, local_y + 1)):
                        continue
                else:
                    is_out_of_bounds = True
                    break

                if not is_out_of_bounds and local_x + 1 < self.__dimensions[0]:
                    if self.__try_to_move(sand, (local_x, local_y), (local_x + 1, local_y + 1)):
                        continue
                else:
                    is_out_of_bounds = True
                    break

                self.__map[local_y][local_x].is_occupied = True
                self.__map[local_y][local_x].is_settled = True
                sand_settled.append(sand)

            for sand in sand_settled:
                self.__sand.remove(sand)
                self.__settled.append(sand)

            i = i + 1

        if part == Part.B:
            self.__min_point = self.__old_min_point
            self.__max_point = self.__old_max_point
            self.__dimensions = self.__old_dimensions
            self.__map = self.__old_map

        return str(len(self.__settled))

    def __print(self) -> None:
        print()
        spawn_x_local, spawn_y_local = self.__to_local(self.__sand_spawn)
        for y, row in enumerate(self.__map):
            line = ''
            for x, tile in enumerate(row):
                tileType = tile.type
                if tileType == TileType.AIR:
                    if y == spawn_y_local and x == spawn_x_local:
                        line = line + '+'
                    elif tile.is_settled:
                        line = line + 'o'
                    elif tile.is_occupied:
                        line = line + '~'
                    else:
                        line = line + '.'
                elif tileType == TileType.ROCK:
                    line = line + '#'
            print(line)
