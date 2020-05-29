import pygame
import numpy as np
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (118, 255, 3)
RED = (255, 87, 51)
GREY = (158, 158, 158)
WINDOW_WIDTH = 1862   # 1880
WINDOW_HEIGHT = 1023  # 1040
BLOCKSIZE = 58  # 4
MARGIN = 2

class Display:

    def __init__(self):
        pygame.init()
        self.grid = np.zeros((WINDOW_WIDTH // (BLOCKSIZE + MARGIN), WINDOW_HEIGHT // (BLOCKSIZE + MARGIN)))
        self.start = (0, 0)
        self.end = (len(self.grid)-1, len(self.grid[0])-1)
        self.grid[self.start[0]][self.start[1]] = 2
        self.grid[self.end[0]][self.end[1]] = 3
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.fill(BLACK)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("A* path finding algorithm")
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
                    pygame.draw.rect(self.screen, GREY, rect)
                elif self.grid[row][column] == 2:
                    pygame.draw.rect(self.screen, GREEN, rect)
                elif self.grid[row][column] == 3:
                    pygame.draw.rect(self.screen, RED, rect)

    def draw_screen(self):

        drawFlag = False
        isRunning = True
        while isRunning:
            
            keysPressed = pygame.key.get_pressed()
            ctrlHeld = keysPressed[pygame.K_LCTRL] or keysPressed[pygame.K_RCTRL]
            shiftHeld = keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_RSHIFT]

            position = pygame.mouse.get_pos()
            row = position[0] // (BLOCKSIZE + MARGIN)
            column = position[1] // (BLOCKSIZE + MARGIN)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    isRunning = False
                    pygame.quit()

                elif event.type == MOUSEBUTTONDOWN and ctrlHeld:
                    if shiftHeld:
                        self.grid[self.end[0]][self.end[1]] = 0
                        self.grid[row][column] = 3
                        self.end = (row, column)
                    else:
                        self.grid[self.start[0]][self.start[1]] = 0
                        self.grid[row][column] = 2
                        self.start = (row, column)
                    drawFlag = True

                elif event.type == MOUSEBUTTONDOWN:
                    self.grid[row][column] = 0 if self.grid[row][column] else 1
                    drawFlag = True

            if drawFlag:
                self.draw_grid()
                pygame.display.update()
                drawFlag = False

            self.clock.tick(60)

def main():
    display = Display()

main()
