from Shared.Solver import Solver, Part


class Day08Solver(Solver):
    def __init__(self, map: list[list[int]], size: (int, int)):
        self.__map = map
        self.__size = size

    def solve(self, part: Part) -> str:
        if part == Part.A:
            return self.solve_a()
        else:
            return self.solve_b()

    def solve_a(self) -> str:
        count = 0
        for y in range(self.__size[1]):
            for x in range(self.__size[0]):
                height = self.__map[y][x]
                seen_from_above = list(self.__map[y2][x] for y2 in range(y+1))
                seen_from_right = list(reversed([self.__map[y][x2] for x2 in range(x, self.__size[0])]))
                seen_from_below = list(reversed([self.__map[y2][x] for y2 in range(y, self.__size[1])]))
                seen_from_left = list(self.__map[y][x2] for x2 in range(x+1))
                if     (max(seen_from_above) == height and seen_from_above.index(height) == y)\
                    or (max(seen_from_right) == height and seen_from_right.index(height) == (self.__size[0] - x - 1))\
                    or (max(seen_from_below) == height and seen_from_below.index(height) == (self.__size[1] - y - 1))\
                    or (max(seen_from_left)  == height and seen_from_left.index(height)  == x):
                    count = count + 1

        return str(count)

    def solve_b(self) -> str:
        max_score = 0
        for y in range(self.__size[1]):
            for x in range(self.__size[0]):
                height = self.__map[y][x]
                seen_above = list(reversed([self.__map[y2][x] for y2 in range(y)]))
                seen_right = list(self.__map[y][x2] for x2 in range(x+1, self.__size[0]))
                seen_below = list(self.__map[y2][x] for y2 in range(y+1, self.__size[1]))
                seen_left = list(reversed([self.__map[y][x2] for x2 in range(x)]))
                try:
                    view_dist_above = [h >= height for h in seen_above].index(True)+1
                except:
                    view_dist_above = len(seen_above)
                try:
                    view_dist_right = [h >= height for h in seen_right].index(True)+1
                except:
                    view_dist_right = len(seen_right)
                try:
                    view_dist_below = [h >= height for h in seen_below].index(True)+1
                except:
                    view_dist_below = len(seen_below)
                try:
                    view_dist_left = [h >= height for h in seen_left].index(True)+1
                except:
                    view_dist_left = len(seen_left)
                score = view_dist_above * view_dist_right * view_dist_below * view_dist_left
                if score > max_score:
                    max_score = score

        return str(max_score)
