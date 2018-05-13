from Main import Main

starting_cell = [3, 3]


def fill_city_map(city_map):
    for row in range(-1, 2):
        for col in range(-1, 2):
            city_map[row + starting_cell[0]][col + starting_cell[1]].contamination_level = 10


def test_calculate_smog_contamination_for_given_cell():
    main = Main(5, 5)
    fill_city_map(main.city_map)
    assert 80 == main.calculate_smog_contamination_for_given_cell(starting_cell[0], starting_cell[1])
