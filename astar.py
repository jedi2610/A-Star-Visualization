import heapq

class Node():
    """
    Represents the data of each walkable cell in A* algorithm
    """

    def __init__(self, x, y, parent=None):
        # Initializes the object with the positions and parent Node
        self.x = x
        self.y = y
        self.parent = parent
        self.set_costs(0, 0)


    def __repr__(self):
        return f'Node value: {self.f}'

    def __lt__(self, other):
        # Required by heapq to compare Node objects
        # Refer - https://stackoverflow.com/a/59956131
        return self.f < other.f

    def set_parent(self, parent):
        # Sets the parent node
        self.parent = parent
        
    def set_costs(self, g, h):
        # Updates the movement cost, heuristic cost and f cost
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
    

def astar(start: tuple, end: tuple):
    
    startNode = Node(start[0], start[1])
    endNode = Node(end[0], end[1])

    openList = []
    closedList = []

    openList.append(startNode)

    while len(openList) != 0:
        pass
