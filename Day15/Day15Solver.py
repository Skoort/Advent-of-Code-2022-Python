import math
from collections import deque
from typing import Optional, Tuple

from Shared.Solver import Solver, Part


class Day15Solver(Solver):
    def __init__(self, sensor_beacon_pairs: list[((int, int), (int, int))]):
        self.__sensor_beacon_pairs = sensor_beacon_pairs

    def solve(self, part: Part) -> str:
        if part == Part.A:
            return self.__solve_a(2000000)
        else:
            return self.__solve_b(4000000)

    def __solve_a(self, global_y) -> str:
        count = 0

        min_blocked_x = math.inf
        max_blocked_x = -math.inf
        sensor_beacon_dists = []
        for sensor, beacon in self.__sensor_beacon_pairs:
            dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            sensor_beacon_dists.append(dist)
            # Calculate the minimum and maximum positions that are potentially blocked.
            min_blocked_x = min(min_blocked_x, sensor[0] - dist)
            max_blocked_x = max(max_blocked_x, sensor[0] + dist)

        for global_x in range(min_blocked_x, max_blocked_x + 1):
            position = global_x, global_y
            if len(list(filter(lambda objects: objects[0] == position or objects[1] == position, self.__sensor_beacon_pairs))) > 0:
                continue
            for i, (sensor, beacon) in enumerate(self.__sensor_beacon_pairs):
                dist_sensor_beacon = sensor_beacon_dists[i]
                dist_sensor_tile = abs(sensor[0] - global_x) + abs(sensor[1] - global_y)
                if dist_sensor_tile <= dist_sensor_beacon:
                    count = count + 1  # There cannot be another beacon in this tile, because it would be closer than this sensor's closest beacon.
                    break

        return str(count)

    def __solve_b(self, max_size) -> str:
        print()

        sensor_beacon_dists = []
        for sensor, beacon in self.__sensor_beacon_pairs:
            dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            sensor_beacon_dists.append(dist)

        for y in range(max_size + 1):
            if y % 50000 == 0:
                print(y)
            ranges = []
            for i, (sensor, beacon) in enumerate(self.__sensor_beacon_pairs):
                # Only one of these intersections should be non empty, unless they both intersect in one point.
                intersect1 = Day15Solver.__intersect_upper(sensor, sensor_beacon_dists[i], y)
                if intersect1 is not None:
                    ranges = Day15Solver.__add_range(ranges, intersect1)
                intersect2 = Day15Solver.__intersect_lower(sensor, sensor_beacon_dists[i], y)
                if intersect2 is not None:
                    ranges = Day15Solver.__add_range(ranges, intersect2)
            if len(ranges) > 1:
                free_x = -1
                for lower, upper in ranges:
                    if lower - 1 >= 0:
                        free_x = lower - 1
                        break
                    if upper + 1 <= max_size:
                        free_x = upper + 1
                        break
                return str(int(4000000 * free_x + y))
        return 'NO SOLUTION'

    @staticmethod
    def __add_range(old_ranges: deque[(int, int)], new_range: (int, int)) -> deque[(int, int)]:
        new_ranges = deque([])
        while len(old_ranges) > 0:
            old_range = old_ranges.popleft()
            if new_range is None or old_range[1] + 1 < new_range[0]:
                new_ranges.append(old_range)
            elif new_range[1] + 1 < old_range[0]:
                new_ranges.append(new_range)
                new_ranges.append(old_range)
                new_range = None
            else:
                new_range = (min(old_range[0], new_range[0]), max(old_range[1], new_range[1]))
        if new_range is not None:
            new_ranges.append(new_range)
        return new_ranges

    @staticmethod
    def __intersect_upper(sensor: (int, int), size: int, target_height: int) -> Optional[Tuple[int, int]]:
        if target_height < sensor[1] or target_height > sensor[1] + size:
            return None  # The target height does not intersect the upper triangle.
        start = sensor[0], sensor[1] + size
        intersect1 = Day15Solver.__find_t(start, +1, target_height) + start[0]
        intersect2 = Day15Solver.__find_t(start, -1, target_height) + start[0]
        return intersect1, intersect2

    @staticmethod
    def __intersect_lower(sensor: (int, int), size: int, target_height: int) -> Optional[Tuple[int, int]]:
        if target_height > sensor[1] or target_height < sensor[1] - size:
            return None  # The target height does not intersect the lower triangle
        start = sensor[0], sensor[1] - size
        intersect1 = Day15Solver.__find_t(start, -1, target_height) + start[0]
        intersect2 = Day15Solver.__find_t(start, +1, target_height) + start[0]
        return intersect1, intersect2

    @staticmethod
    def __find_t(start: (int, int), slope: int, target_height: int):
        result = (target_height - start[1]) / slope
        return result
