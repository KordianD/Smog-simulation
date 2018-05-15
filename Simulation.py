from Main import Main
from Plotter import Plotter

simulation = Main(100, 100)

simulation.start_simulation(10)


Plotter.plot_city_map_contamination_level(simulation.city_map)