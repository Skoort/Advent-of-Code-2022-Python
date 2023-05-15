from Day12.Day12Solver import Day12Solver
from Day12.Edge import Edge
from Day12.Node import Node
from Shared.Parser import Parser


class Day12Parser(Parser):
    def get_solver(self, text: str) -> Day12Solver:
        map = []
        start_pos = (0, 0)
        end_pos = (0, 0)

        # Construct nodes.
        for y, line in enumerate(text.strip().split('\n')):
            row = []
            for x, c in enumerate(line):
                if c.islower():
                    height = ord(c) - ord('a') + 1
                elif c == 'S':
                    height = 1
                    start_pos = (x, y)
                elif c == 'E':
                    height = 26
                    end_pos = (x, y)
                row.append(Node(x, y, height))
            map.append(row)

        # Construct edges.
        for y in range(len(map)):
            for x in range(len(map[0])):
                node = map[y][x]
                edges = []
                if y > 0:
                    edges.append(Edge(node, map[y-1][x], 1))
                if y < len(map) - 1:
                    edges.append(Edge(node, map[y+1][x], 1))
                if x > 0:
                    edges.append(Edge(node, map[y][x-1], 1))
                if x < len(map[0]) - 1:
                    edges.append(Edge(node, map[y][x+1], 1))
                node.edges = edges

        start = map[start_pos[1]][start_pos[0]]
        end = map[end_pos[1]][end_pos[0]]

        return Day12Solver(map, start, end)
