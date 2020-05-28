from heapq import heappop, heappush

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
    

def manhattan_distance(source, goal):
    return abs(source[0] - goal[0]) + abs(source[1] - goal[1])

def return_index(items, position):
    for i, item in enumerate(items):
        if item.position == position:
            return i

def astar(maze, start: tuple, end: tuple):
    
    startNode = Node(start)
    endNode = Node(end)

    openList = []
    closedList = []
    openListPositions = []
    path = []
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        print("Start and end points should in a walkable terrain")
        return path

    heappush(openList, startNode)
    openListPositions.append(startNode.position)

    while len(openList) != 0:

        currentNode = heappop(openList)
        closedList.append(currentNode.position)
        openListPositions.remove(currentNode.position)

        if currentNode.position == endNode.position:
            while currentNode.parent != None:
                path.append(currentNode)
                currentNode = currentNode.parent
            path.append(startNode)
            return path[::-1]
        
        for neighbour in neighbours:

            position = (currentNode.position[0] + neighbour[0], currentNode.position[1] + neighbour[1])
            x, y = position
            if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == 1:
                continue
            else:
                childNode = Node(position, currentNode)
    
            if childNode.position in closedList:
                continue

            if neighbour in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
                childNode.isDiagnol = True

            gCost = currentNode.gCost + HORIZONTALCOST if not(childNode.isDiagnol) else currentNode.gCost + DIAGNOLCOST
            hCost = manhattan_distance(childNode.position, endNode.position)
            childNode.set_costs(gCost, hCost)

            if position in openListPositions:
                index = return_index(openList, position)
                if gCost < openList[index].gCost:
                    del openList[index]
                    heappush(openList, childNode)
            else:
                heappush(openList, childNode)
                openListPositions.append(childNode.position)

    return path
