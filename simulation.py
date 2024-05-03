from grid import Grid


class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.grid.fill_random()

    def draw(self, window):
        self.grid.draw(window)

    def count_live_neighbors(self, grid, row, col):
        live_neighbors = 0
        neightbor_offsets = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for offset in neightbor_offsets:
            new_row = (row + offset[0]) % self.rows
            new_col = (col + offset[1]) % self.cols
            if self.grid.cells[new_row][new_col] == 1:
                live_neighbors += 1

        return live_neighbors

    def update(self):
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = self.count_live_neighbors(self.grid, row, col)
                cell_value = self.grid.cells[row][col]

                if cell_value == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        self.temp_grid.cells[row][col] = 0
                    else:
                        self.temp_grid.cells[row][col] = 1
                else:
                    if live_neighbors == 3:
                        self.temp_grid.cells[row][col] = 1
                    else:
                        self.temp_grid.cells[row][col] = 0

        for row in range(self.rows):
            for col in range(self.cols):
                self.grid.cells[row][col] = self.temp_grid.cells[row][col]
