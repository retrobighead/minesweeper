class Cell:
    def __init__(self, has_bomb):
        self.is_covered = True
        self.has_bomb = has_bomb
        self.has_flag = False

    def step(self):
        self.is_covered = False

    def set_flag(self):
        self.has_flag = True