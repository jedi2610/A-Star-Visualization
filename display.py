import pygame
import numpy as np
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (178, 255, 89)
WINDOW_WIDTH = 1862   # 1880
WINDOW_HEIGHT = 1023  # 1040
BLOCKSIZE = 58  # 4
MARGIN = 2

class Display:

    def __init__(self):
        pygame.init()
        # self.grid = [[0] * (WINDOW_HEIGHT // BLOCKSIZE)] * (WINDOW_WIDTH // BLOCKSIZE)
        self.grid = np.zeros((WINDOW_WIDTH // (BLOCKSIZE + MARGIN), WINDOW_HEIGHT // (BLOCKSIZE + MARGIN)))
        print(len(self.grid), len(self.grid[0]))
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), RESIZABLE)
        pygame.display.set_caption("A* Path finding algorithm")
        self.screen.fill(BLACK)
        self.clock = pygame.time.Clock()
        self.draw_grid()
        pygame.display.update()
        self.draw_screen()
        
    def return_grid(self):
        return self.grid

    def draw_grid(self):
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                rect = pygame.Rect((MARGIN + BLOCKSIZE) * row + MARGIN,(MARGIN + BLOCKSIZE) * column + MARGIN, BLOCKSIZE, BLOCKSIZE)
                if self.grid[row][column] == 0:
                    pygame.draw.rect(self.screen, WHITE, rect)
                elif self.grid[row][column] == 1:
                    pygame.draw.rect(self.screen, GREEN, rect)

    def draw_screen(self):

        drawFlag = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    row = position[0] // (BLOCKSIZE + MARGIN)
                    column = position[1] // (BLOCKSIZE + MARGIN)
                    self.grid[row][column] = 0 if self.grid[row][column] else 1
                    drawFlag = True

            if drawFlag:
                self.draw_grid()
                # rect = pygame.Rect((MARGIN + BLOCKSIZE) * row + MARGIN,(MARGIN + BLOCKSIZE) * column + MARGIN, BLOCKSIZE, BLOCKSIZE)
                # pygame.draw.rect(self.screen, GREEN, rect)
                pygame.display.update()
                drawFlag = False

            self.clock.tick(60)

def main():
    display = Display()

main()
