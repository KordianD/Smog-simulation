from Main import Main
from Plotter import Plotter

simulation = Main(10, 10)
simulation.read_map()
simulation.start_simulation(40)

Plotter.plot_city_map_contamination_level(simulation.city_map)