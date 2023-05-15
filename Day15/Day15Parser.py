import math

from Day15.Day15Solver import Day15Solver
from Shared.Parser import Parser


class Day15Parser(Parser):
    def get_solver(self, text: str) -> Day15Solver:
        sensor_beacon_pairs = []
        for line in text.strip().split('\n'):
            part1, part2 = line.split(':')
            sensor = tuple(int(assignment.split('=')[1]) for assignment in part1.replace('Sensor at', '').split(','))
            beacon = tuple(int(assignment.split('=')[1]) for assignment in part2.replace('closest beacon is at', '').split(','))
            sensor_beacon_pairs.append((sensor, beacon))

        return Day15Solver(sensor_beacon_pairs)
