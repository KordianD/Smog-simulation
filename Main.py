from copy import deepcopy
from random import randint
from Plotter import Plotter
from Cell import Cell
from Point import Point
from scipy import misc
from configuration import *

class Main:
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.number_of_stoves = int(map_height * map_width * STOVE_PRODUCTION_PERCENTAGE)       # KUCHENKI
        self.city_map = [[Cell() for _ in range(self.map_width)] for _ in range(map_height)]
        self.stove_coordinates = [Point(randint(0, map_height - 1), randint(0, self.map_width - 1))
                                  for _ in range(self.number_of_stoves)]
        self.__initialize_cells()

    def __initialize_cells(self):
        for stove in self.stove_coordinates:
            self.city_map[stove.x][stove.y].change_level_of_smog_production(STOVE_SMOG_PRODUCTION)

    def start_simulation(self, number_of_iteration):
        for iteration in range(number_of_iteration):
            print("Number of iteration " + str(iteration + 1))
            self.update_map()
            #Plotter.plot_city_map_contamination_level(self.city_map)

    def update_map(self):
        first_map = deepcopy(self.city_map)

        for row in range(self.map_height):
            for col in range(self.map_width):
                smog_contamination = self.calculate_smog_contamination_for_given_cell(row, col)  #niewielkie zmiany majace ograniczyc uciekanie do nieskonczonosci
                first_map[row][col].contamination_level = smog_contamination
                first_map[row][col].smog_production = self.city_map[row][col].smog_production

        self.substitute_map(first_map)

    def substitute_map(self, first_map):
        self.city_map = first_map
        #!!!!!!!!!!!!!!!!!!!!!!
        #USUNALEM DEEPCOPY, chyba nie było konieczne, przyspiesza symulacje

    def calculate_smog_contamination_for_given_cell(self, row, col): #JUTRO OPISZE CO TU ZROBILEM :)
        sum = self.city_map[row][col].smog_production
        old = self.city_map[row][col].contamination_level
        COEFF=SPREAD_COEFFICIENT*HUMIDITY/(WIND*RAIN)
        temp=[]
        for i in range(-2, 3):      #POPRAWIONY NA WIEKSZY
            for j in range(-2, 3):
                if self.is_position_valid(row, col, i, j):
                    source = WIND_DIR[2+i][2+j]*self.city_map[row + i][col + j].contamination_level
                    temp.append(source)
        temp.sort()
        #temp.reverse()
        for k in range(len(temp)):
            if sum +COEFF*temp[k] < FLOW_RESISTANCE*temp[k]:
                sum+= COEFF*temp[k]
            elif sum < temp[k]:
                sum=FLOW_RESISTANCE*temp[k]

        return sum

    def is_position_valid(self, row, col, i, j):
        return 0 <= row + i < self.map_height and 0 <= col + j < self.map_width and (i != 0 or j != 0)

    def read_map(self):
        img = misc.imread("input.png")
        img = 255-img
        width = img.shape[1]
        height = img.shape[0]
        print(width)
        print(height)
        self.map_width = width
        self.map_height = height
        self.city_map = [[Cell() for _ in range(width)] for _ in range(height)]


        for row in range(height):
            for col in range(width):
                self.city_map[row][col].smog_production = img[row][col][1]
        #nie rysuje całej mapki