from Main import Main
from Plotter import Plotter

simulation = Main(20, 20)

simulation.start_simulation(20)


Plotter.plot_city_map_contamination_level(simulation.city_map)