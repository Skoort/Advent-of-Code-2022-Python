from __future__ import annotations

import Day07.FileSystemObject as FileSystemObjectModule


class Directory(FileSystemObjectModule.FileSystemObject):
    def __init__(self, name: str, parent: Directory):
        self.__name = name
        self.__parent = parent
        self.contents = {}

    def get(self, path):
        path = path.strip('/')
        if path == '':
            return self

        args = path.split('/')
        rest = '/'.join(args[1:])
        if args[0] == '..':
            return self.__parent.get(rest)
        else:
            return self.contents[args[0]].get(rest)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def size(self) -> int:
        return sum(map(lambda x: x.size, self.contents.values()))

    @property
    def parent(self) -> Directory:
        return self.__parent
