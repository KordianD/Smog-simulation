from copy import deepcopy
from random import randint

from Cell import Cell
from Point import Point
from configuration import *


class Main:
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.number_of_stoves = int(map_height * map_width * STOVE_PRODUCTION_PERCENTAGE)
        self.city_map = [[Cell() for _ in range(self.map_width)] for _ in range(map_height)]
        self.stove_coordinates = [Point(randint(0, map_height - 1), randint(0, self.map_width - 1))
                                  for _ in range(self.number_of_stoves)]
        self.__initialize_cells()

    def __initialize_cells(self):
        for stove in self.stove_coordinates:
            self.city_map[stove.x][stove.y].change_level_of_smog_production(STOVE_SMOG_PRODUCTION)

    def start_simulation(self, number_of_iteration):
        for _ in range(number_of_iteration):
            self.update_map()

    def update_map(self):
        first_map = deepcopy(self.city_map)

        for row in range(self.map_height):
            for col in range(self.map_height):
                smog_contamination = self.calculate_smog_contamination_for_given_cell(row, col) + self.city_map[row][col].smog_production
                first_map[row][col].contamination_level = smog_contamination

        self.substitute_map(first_map)

    def substitute_map(self, first_map):
        self.city_map = deepcopy(first_map)

    def calculate_smog_contamination_for_given_cell(self, row, col):
        sum = 0
        for i in range(-1, 2):
            sum += self.calculate_smog_contamination_for_given_cell_row(row, col, i)

        return sum

    def calculate_smog_contamination_for_given_cell_row(self, row, col, i):
        sum = 0
        for j in range(-1, 2):
            if self.is_position_valid(row, col, i, j):
                sum += self.city_map[row + i][col + j].contamination_level

        return sum

    def is_position_valid(self, row, col, i, j):
        return 0 <= row + i < self.map_height and 0 <= col + j < self.map_height and (i != 0 or j != 0)
