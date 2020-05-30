import pygame
import numpy as np
from time import sleep
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (118, 255, 3)
RED = (255, 87, 51)
GREY = (158, 158, 158)
LIME = (198, 255, 0)
TEAL = (178, 223, 219)
DARK_GREEN = (129, 199, 132)
LIGHT_GREY = (232, 234, 246)
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
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display.fill(BLACK)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("A* path finding algorithm")
        
    def return_start_and_end(self):
        return (self.start, self.end)

    def return_grid(self):
        return self.grid

    def draw_grid(self):
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                rect = pygame.Rect((MARGIN + BLOCKSIZE) * row + MARGIN,(MARGIN + BLOCKSIZE) * column + MARGIN, BLOCKSIZE, BLOCKSIZE)
                if self.grid[row][column] == 0:
                    pygame.draw.rect(self.display, WHITE, rect)
                elif self.grid[row][column] == 1:
                    pygame.draw.rect(self.display, GREY, rect)
                elif self.grid[row][column] == 2:
                    pygame.draw.rect(self.display, GREEN, rect)
                elif self.grid[row][column] == 3:
                    pygame.draw.rect(self.display, RED, rect)

    def draw_screen(self):

        self.draw_grid()
        pygame.display.update()
        drawFlag = False
        isRunning = True
        while isRunning:

            keysPressed = pygame.key.get_pressed()
            ctrlHeld = keysPressed[pygame.K_LCTRL] or keysPressed[pygame.K_RCTRL]
            shiftHeld = keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_RSHIFT]
            altHeld = keysPressed[pygame.K_LALT] or keysPressed[pygame.K_RALT]
            enterHeld = keysPressed[pygame.K_RETURN] or keysPressed[pygame.K_KP_ENTER]

            position = pygame.mouse.get_pos()
            row = position[0] // (BLOCKSIZE + MARGIN)
            column = position[1] // (BLOCKSIZE + MARGIN)

            for event in pygame.event.get():

                if event.type == pygame.QUIT or keysPressed[pygame.K_ESCAPE] or (altHeld and keysPressed[pygame.K_F4]):
                    isRunning = False
                    pygame.quit()

                elif enterHeld and ctrlHeld:
                    isRunning = False
                    break
                
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

    def update_screen(self, openListPositions, closedListPositions):
          
        for position in openListPositions:
            row, column = position
            rect = pygame.Rect((MARGIN + BLOCKSIZE) * row + MARGIN, (MARGIN + BLOCKSIZE) * column + MARGIN, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(self.display, LIGHT_GREY, rect)

        for position in closedListPositions:
            row, column = position
            rect = pygame.Rect((MARGIN + BLOCKSIZE) * row + MARGIN, (MARGIN + BLOCKSIZE) * column + MARGIN, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(self.display, LIME, rect, 2)

        pygame.display.update()
        # sleep(0.01)

    def draw_path(self, path):
        for position in path:
            row, column = position
            rect = pygame.Rect((MARGIN + BLOCKSIZE) * row + MARGIN, (MARGIN + BLOCKSIZE) * column + MARGIN, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(self.display, DARK_GREEN, rect)
            pygame.display.update()
        rect = pygame.Rect((MARGIN + BLOCKSIZE) * row + MARGIN, (MARGIN + BLOCKSIZE) * column + MARGIN, BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(self.display, RED, rect)
        pygame.display.update()

    def display_not_found(self):

        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('No path found', True, RED, BLACK)
        textRect = text.get_rect()
        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.display.blit(text, textRect)
        pygame.display.update()

    def dummy_cycle(self):

        isRunning = True
        while isRunning:
            keysPressed = pygame.key.get_pressed()
            altHeld = keysPressed[pygame.K_LALT] or keysPressed[pygame.K_RALT]

            for event in pygame.event.get():
                    if event.type == pygame.QUIT or keysPressed[pygame.K_ESCAPE] or (altHeld and keysPressed[pygame.K_F4]):
                        isRunning = False
                        pygame.quit()
