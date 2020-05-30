import argparse
from search import *
from display import *

def main(args):

    isDiagnolsAllowed = args.diagnol
    heuristic = args.heuristic
    displayObject = Display()
    displayObject.draw_screen()
    maze = displayObject.return_grid()
    start, end = displayObject.return_start_and_end()
    astar = AStar(maze, start, end, displayObject, heuristic, isDiagnolsAllowed)
    path = astar.return_path()
    if len(path) != 0:
        displayObject.draw_path(path)
    else:
        displayObject.display_not_found()
    displayObject.dummy_cycle()

    if args.command:
        if len(path) == 0:
            print("No path")
        else:
            path.pop(len(path)-1)
            for i in range(len(maze[0])):
                for j in range(len(maze)):
                    if (j, i) in path:
                        print("*", end=" ")
                    elif maze[j][i] == 1:
                        print("|", end=" ")
                    elif maze[j][i] == 2:
                        print("F", end=" ")
                    elif maze[j][i] == 3:
                        print("T", end=" ")
                    else:
                        print(".", end=" ")
                print("\n")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Visualization of the A* algorithm")
    parser.add_argument('-c', '--command', dest='command', default=False, action='store_true', help="Displays the path in the command line")
    parser.add_argument('-d', '--diagnol', dest='diagnol', default=True, action='store_false', help="Disable diagnol traversal while finding path")
    parser.add_argument('--heuristic', dest='heuristic', default='d', choices=['m', 'e', 'd'], help="Specify the method for calculating the heuristic cost. 'd' is recommened if diagnol traversal is allowed.")
    args = parser.parse_args()
    main(args)
