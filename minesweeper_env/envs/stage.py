from minesweeper_env.envs.cell import Cell

import random
import numpy as np

class Stage:
    def __init__(self, width=9, height=9, bomb_count=10):
        self.width = width
        self.height = height
        self.bomb_count = bomb_count
        self.reset_cells()
        self.remain_cells = self.width * self.height

    def reset(self):
        self.remain_cells()
        self.remain_cells = self.width * self.height

    def decrement_cell(self):
        self.remain_cells -= 1

    def get_bomb_indexes(self):
        indexes = []
        for w in range(self.width):
            for h in range(self.height):
                indexes.append((w, h))
        return random.sample(indexes, self.bomb_count)

    def reset_cells(self):
        self.bomb_indexes = self.get_bomb_indexes()
        self.cells = []
        for y in range(self.height):
            self.cells.append([])
            for x in range(self.width):
                cell = None
                if (x, y) in self.bomb_indexes:
                    cell = Cell(True)
                else:
                    cell = Cell(False)
                self.cells[-1].append(cell)

    def get_cell(self, x, y):
        in_range = 0 <= x and x < self.width and 0 <= y and y < self.height
        if not in_range:
            return None

        return self.cells[y][x]

    def get_surrounded_count(self, x, y):
        indexes = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
        is_in_range = lambda x, y: 0 <= x and x < self.width and 0 <= y and y < self.height
        filtered_indexes = filter(lambda ele: is_in_range(ele[0], ele[1]), indexes)
        surrounded_cells = [self.get_cell(x, y) for x, y in filtered_indexes]
        return sum([cell.has_bomb for cell in surrounded_cells])