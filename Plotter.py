import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot_city_map_smog_production_level(city_map):
        contamination_map = Plotter.convert_to_numeric_map_smog_production_level(city_map)
        Plotter.plot_city_map(contamination_map)

    @staticmethod
    def plot_city_map_contamination_level(city_map):
        contamination_map = Plotter.convert_to_numeric_map_contamination_level(city_map)
        Plotter.plot_city_map(contamination_map)

    @staticmethod
    def convert_to_numeric_map_contamination_level(city_map):
        return [[city_map[row][col].contamination_level for col in range(len(city_map[0]))] for row in range(len(city_map))]

    @staticmethod
    def convert_to_numeric_map_smog_production_level(city_map):
        return [[city_map[row][col].smog_production for col in range(len(city_map[0]))] for row in range(len(city_map))]

    @staticmethod
    def plot_city_map(city_map):
        plt.matshow(city_map)
        plt.show()
