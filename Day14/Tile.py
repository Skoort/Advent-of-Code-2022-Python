from enum import Enum


class TileType(Enum):
    AIR = 0,
    ROCK = 1,


class Tile:
    def __init__(self, x: int, y: int, tileType: TileType):
        self.x = x
        self.y = y
        self.type = tileType
        self.__reset()

    def __reset(self) -> None:
        self.is_settled = False
        self.is_occupied = True if self.type == TileType.ROCK else False
        self.visit_count = 0
