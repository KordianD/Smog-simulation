from random import randint

from Cell import Cell
from Point import Point
from configuration import *


class Main:
    def __init__(self):
        self.city_map = [[Cell() for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.stove_coordinates = [Point(randint(0, MAP_HEIGHT - 1), randint(0, MAP_WIDTH - 1))
                                  for _ in range(NUMBER_OF_STOVES)]
        self.__initialize_cells()

    def __initialize_cells(self):
        for stove in self.stove_coordinates:
            self.city_map[stove.x][stove.y].change_level_of_smog_production(STOVE_SMOG_PRODUCTION)
