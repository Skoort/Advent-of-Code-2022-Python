from collections import deque

from Day07.Directory import Directory
from Shared.Solver import Solver, Part


class Day07Solver(Solver):
    def __init__(self, directory: Directory):
        self.__directory = directory

    def solve(self, part: Part) -> str:
        if part == Part.A:
            return str(sum(map(lambda x: x.size, Day07Solver.traverse(self.__directory))))
        else:
            total_size = 70000000
            required_space = 30000000
            current_space = total_size - self.__directory.size
            space_to_free = max(required_space - current_space, 0)
            return Day07Solver.traverse2(self.__directory, space_to_free).size

    @staticmethod
    def traverse(directory: Directory) -> list[Directory]:
        folders = []
        if directory.size < 100000:
            folders.append(directory)
        for obj in directory.contents.values():
            if isinstance(obj, Directory):
                folders = folders + Day07Solver.traverse(obj)

        return folders

    @staticmethod
    def traverse2(directory: Directory, space_to_free: int) -> Directory:
        candidates = []

        to_search = deque([directory])
        while len(to_search) > 0:
            folder = to_search.popleft()
            if folder.size > space_to_free:
                candidates.append(folder)
                for obj in folder.contents.values():
                    if isinstance(obj, Directory):
                        to_search.append(obj)

        return [x for x in candidates if x.size > space_to_free][-1]


