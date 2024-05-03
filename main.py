import pygame, sys
from simulation import Simulation

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_hEIGHT = 1000
CELL_SIZE = 5
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_hEIGHT))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

simulation = Simulation(WINDOW_WIDTH, WINDOW_hEIGHT, CELL_SIZE)

# Simulation Loop
while True:

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updating State
    simulation.update()

    # 3. Drawing
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)
