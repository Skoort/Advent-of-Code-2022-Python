from collections import deque

from Day12.Node import Node
from Shared.Solver import Solver, Part


class Day12Solver(Solver):
    def __init__(self, map: list[list[Node]], start: Node, end: Node):
        self.__map = map
        self.__start = start
        self.__end = end

    def solve(self, part: Part) -> str:
        self.__reset()

        to_visit = deque([(self.__start if part == Part.A else self.__end, None)])
        found = None
        while len(to_visit) > 0:
            curr_node, from_node = to_visit.popleft()
            x, y = curr_node.x, curr_node.y
            if self.__visit_map[y][x][0]:
                continue

            self.__visit_map[y][x] = (True, from_node)

            if     (part == Part.A and curr_node == self.__end)\
                or (part == Part.B and curr_node.height == 1):
                found = curr_node
                break

            for next_node in map(lambda edge: edge.node_to, curr_node.edges):
                if     (part == Part.A and next_node.height <= curr_node.height + 1)\
                    or (part == Part.B and curr_node.height <= next_node.height + 1):
                    to_visit.append((next_node, curr_node))

        if not found:
            return '-1'

        path = [found]
        while True:
            from_node = self.__visit_map[path[-1].y][path[-1].x][1]
            if from_node is None:
                break
            path.append(from_node)

        return str(len(path) - 1)

    def __reset(self) -> None:
        self.__visit_map = [[(False, None) for _ in row] for row in self.__map]
