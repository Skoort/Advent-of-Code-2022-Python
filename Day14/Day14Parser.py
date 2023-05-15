from Day14.Day14Solver import Day14Solver
from Day14.Tile import Tile, TileType
from Shared.Parser import Parser


class Day14Parser(Parser):
    def get_solver(self, text: str) -> Day14Solver:
        min_point = (500, 0)
        max_point = (500, 0)
        lines = []
        for line in text.strip().split('\n'):
            row = []
            for point in line.split('->'):
                x, y = map(lambda text: int(text), point.split(','))
                min_point = (min(x, min_point[0]), min(y, min_point[1]))
                max_point = (max(x, max_point[0]), max(y, max_point[1]))
                row.append((x, y))
            lines.append(row)
        dimensions = (max_point[0] - min_point[0] + 1, max_point[1] - min_point[1] + 1)
        tilemap = [[Tile(x + min_point[0], y + min_point[1], TileType.AIR) for x in range(dimensions[0])] for y in range(dimensions[1])];
        for points in lines:
            for i in range(len(points) - 1):
                point1 = points[i]
                point2 = points[i + 1]
                # Based on input, one of these distances will be zero.
                delta_x, delta_y = point2[0] - point1[0], point2[1] - point1[1]
                num_steps = max(abs(delta_x), abs(delta_y)) + 1
                for t in range(num_steps):
                    x = point1[0] + round(delta_x * t / (num_steps - 1))
                    y = point1[1] + round(delta_y * t / (num_steps - 1))
                    tile = tilemap[y - min_point[1]][x - min_point[0]]
                    tile.type = TileType.ROCK
                    tile.is_occupied = True

        return Day14Solver(min_point, max_point, dimensions, tilemap, (500, 0))
