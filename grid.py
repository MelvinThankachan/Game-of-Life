import pygame, random


class Grid:

    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for col in range(self.cols):
                color = (0, 255, 0) if self.cells[row][col] == 1 else (0, 0, 0)
                pygame.draw.rect(
                    window,
                    color,
                    (
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

    def fill_random(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col] = random.choice([0, 1])
