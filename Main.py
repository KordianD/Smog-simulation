from random import randint

from Cell import Cell
from Point import Point
from configuration import *

stove_coordinates = [Point(randint(0, MAP_HEIGHT - 1), randint(0, MAP_WIDTH - 1)) for _ in range(NUMBER_OF_STOVES)]

city_map = [[Cell() for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
