import argparse
from search import *
from display import *

def main():

    displayObject = Display()
    displayObject.draw_screen()
    maze = displayObject.return_grid()
    start, end = displayObject.return_start_and_end()
    astar = AStar(maze, start, end, displayObject)
    path = astar.return_path()
    displayObject.draw_path(path)
    displayObject.dummy_cycle()

    # if len(path) == 0:
    #     print("No path")
    # else:
    #     for i in range(len(maze)):
    #         for j in range(len(maze[0])):
    #             if (i, j) in path:
    #                 print("*", end=" ")
    #             elif maze[i][j] == 1:
    #                 print("|", end=" ")
    #             else:
    #                 print("-", end=" ")
    #         print("\n")

if __name__ == "__main__":
    main()
