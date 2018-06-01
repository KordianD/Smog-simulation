class Cell:
    smog_production: int

    def __init__(self, contamination_level=0, smog_production=0):
        self.contamination_level = contamination_level
        self.smog_production = smog_production

    def change_level_of_smog_production(self, change_level):
        self.smog_production += change_level

    def new_level_of_smog_production(self, new_level):
        self.smog_production = new_level

