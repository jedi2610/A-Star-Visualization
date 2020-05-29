import argparse
from search import *
# from display import *

def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    path = AStar(maze, (0, 0), (0, 9)).return_path()
    if len(path) == 0:
        print("No path")
    else:
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (i, j) in path:
                    print("*", end=" ")
                elif maze[i][j] == 1:
                    print("|", end=" ")
                else:
                    print("-", end=" ")
            print("\n")

if __name__ == "__main__":
    main()
