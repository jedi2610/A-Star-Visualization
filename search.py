from heapq import heappop, heappush
from time import sleep
from display import *

HORIZONTALCOST = 10
DIAGNOLCOST = 14
class Node():
    """
    Represents the data of each walkable cell in A* algorithm
    """

    def __init__(self, position, parent=None):
        # Initializes the object with the positions and parent Node
        self.position = position
        self.parent = parent
        self.isDiagnol = False
        self.set_costs(0, 0)

    def __repr__(self):
        return f'Position: {self.position}\n'
        # \nG Cost: {self.gCost}\nH Cost: {self.hCost}\nF Cost: {self.fCost}\n

    def __lt__(self, other):
        # Required by heapq to compare Node objects
        # Refer - https://stackoverflow.com/a/59956131
        return self.fCost < other.fCost

    def set_parent(self, parent):
        # Sets the parent node
        self.parent = parent
        
    def set_costs(self, gCost, hCost):
        # Updates the movement cost, heuristic cost and f cost
        self.gCost = gCost
        self.hCost = hCost
        self.fCost = self.gCost + self.hCost
    

class AStar:

    def __init__(self, isNeighboursAllowed=True):
        self.openList = []
        self.closedList = []
        self.openListPositions = []
        self.path = []
        self.screen = Display()
        self.maze = self.screen.return_grid()
        self.startPosition, self.endPosition = self.screen.return_start_and_end()
        self.isNeighboursAllowed = isNeighboursAllowed
        self.startNode = Node(self.startPosition)
        self.endNode = Node(self.endPosition)
        self.find_path()

    def manhattan_distance(self, source, goal):
        return abs(source[0] - goal[0]) + abs(source[1] - goal[1])

    def return_index(self, items, position):
        for i, item in enumerate(items):
            if item.position == position:
                return i

    def return_path(self):
        return self.path

    def find_path(self):

        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if self.isNeighboursAllowed:
            neighbours.extend([(-1, -1), (1, -1), (-1, 1), (1, 1)])

        if self.maze[self.startPosition[0]][self.startPosition[1]] == 1 or self.maze[self.endPosition[0]][self.endPosition[1]] == 1:
            print("Start and end points should in a walkable terrain")
            return path

        heappush(self.openList, self.startNode)
        self.openListPositions.append(self.startNode.position)

        while len(self.openList) != 0:

            currentNode = heappop(self.openList)
            self.closedList.append(currentNode.position)
            self.openListPositions.remove(currentNode.position)

            if currentNode.position == self.endNode.position:
                while currentNode.parent != None:
                    self.path.append(currentNode.position)
                    currentNode = currentNode.parent
                # self.path.pop(0)
                self.path = self.path[::-1]
                self.screen.draw_path(self.path)
                sleep(20)
            
            for neighbour in neighbours:

                position = (currentNode.position[0] + neighbour[0], currentNode.position[1] + neighbour[1])
                x, y = position
                if x < 0 or y < 0 or x >= len(self.maze) or y >= len(self.maze[0]) or self.maze[x][y] == 1:
                    continue
                else:
                    childNode = Node(position, currentNode)
        
                if childNode.position in self.closedList:
                    continue

                if neighbour in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
                    childNode.isDiagnol = True

                gCost = currentNode.gCost + HORIZONTALCOST if not(childNode.isDiagnol) else currentNode.gCost + DIAGNOLCOST
                hCost = self.manhattan_distance(childNode.position, self.endNode.position)
                childNode.set_costs(gCost, hCost)

                if position in self.openListPositions:
                    index = self.return_index(self.openList, position)
                    if gCost < self.openList[index].gCost:
                        del self.openList[index]
                        heappush(self.openList, childNode)
                else:
                    heappush(self.openList, childNode)
                    self.openListPositions.append(childNode.position)

            self.screen.update_screen(self.openListPositions, self.closedList)
            # sleep(1)
