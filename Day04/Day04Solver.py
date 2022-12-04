from Shared.Solver import Solver, Part


class Day04Solver(Solver):
    def __init__(self, pairs: list[((int, int), (int, int))]):
        self.__pairs = pairs

    def solve(self, part: Part) -> str:
        count = 0
        for pair in self.__pairs:
            r1 = pair[0]
            r2 = pair[1]
            if part == Part.A:
                # How many times does one of the ranges fully contain the other?
                if (r2[0] <= r1[0] and r1[1] <= r2[1]) or \
                   (r1[0] <= r2[0] and r2[1] <= r1[1]):
                    count = count + 1
            else:
                # How many times do they overlap at all?
                # if len(set(range(r1[0], r1[1]+1)) & set(range(r2[0], r2[1]+1))) > 0:
                if (r1[0] >= r2[0] and r1[0] <= r2[1]) or \
                   (r2[0] >= r1[0] and r2[0] <= r1[1]):
                    count = count + 1

        return count
