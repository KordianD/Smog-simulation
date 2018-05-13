from copy import deepcopy
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

    def update_map(self):
        first_map = deepcopy(self.city_map)

        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                smog_contamination = self.calculate_smog_contamination_for_given_cell(row, col)
                first_map[row][col].contamination_level = smog_contamination

    def calculate_smog_contamination_for_given_cell(self, row, col):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < MAP_HEIGHT and 0 <= col + j < MAP_WIDTH and (i != 0 and j != 0):
                    sum += self.city_map[row + i][col + i].contamination_level
                    # TODO: ADD UNIT TESTS TO THIS

        return sum
