from abc import ABC, abstractmethod


class FileSystemObject(ABC):
    @property
    @abstractmethod
    def name(self) -> int:
        pass

    @property
    @abstractmethod
    def size(self) -> int:
        pass

    @property
    @abstractmethod
    def parent(self):
        pass


if __name__ == '__main__':
    print('Running FileSystemObject.py unit tests.')

    threw = False
    try:
        parser = FileSystemObject()
    except:
        threw = True
    if not threw:
        assert False

    print('Unit tests successful.')
