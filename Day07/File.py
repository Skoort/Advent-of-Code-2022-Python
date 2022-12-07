import Day07.Directory as DirectoryModule
import Day07.FileSystemObject as FileSystemObjectModule


class File(FileSystemObjectModule.FileSystemObject):
    def __init__(self, name: str, size: int, parent):
        self.__name = name
        self.__size = size
        self.__parent = parent

    @property
    def name(self) -> str:
        return self.__name

    @property
    def size(self) -> int:
        return self.__size

    @property
    def parent(self) -> DirectoryModule.Directory:
        return self.__parent
