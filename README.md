# A-Star-Visualization
> A visualization of the A* search algorithm using pygame.

## Usage
```
usage: app.py [-h] [-c] [-d] [--heuristic {m,e,d}]

Visualization of the A* algorithm

optional arguments:
  -h, --help           show this help message and exit
  -c, --command        Displays the path in the command line
  -d, --diagnol        Disable diagnol traversal while finding path
  --heuristic {m,e,d}  Specify the method for calculating the heuristic cost.
                       'd' is recommened if diagnol traversal is allowed.
```

* Use <kbd>Ctrl</kbd> + right click to place the starting block.
* Use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + right click to place the ending block.
* Use right click to place blocks.
* Use <kbd>Ctrl</kbd> + <kbd>Enter</kbd> to start the A* search.
* Boxes outlined with green color are present in the closed list.
* Boxes filled with light grey are present in the open list.

## Demo

![nopathdemo](images/nopathdemo.gif)

## Supported heuristic methods

### Manhattan distance (m)
```python
def manhattan_distance(self, source, goal):
        return (abs(source[0] - goal[0]) + abs(source[1] - goal[1])) * HORIZONTALCOST
```
### Euclidean distance (e)
```python
def euclidean_distance(self, source, goal):
        return sqrt(pow(abs(source[0] - goal[0]), 2) + pow(abs(source[1] - goal[1]), 2)) * HORIZONTALCOST
```
From the A* pages of Amit:

> I’ve seen several A* web pages recommend that you avoid the expensive square root in the Euclidean distance by using distance-squared. **DO NOT DO THIS!** This definitely runs into the scale problem. The scale of g and h need to match, because you’re adding them together to form f. When A* computes f(n) = g(n) + h(n), the square of distance will be much higher than the cost g and you will end up with an overestimating heuristic. For longer distances, this will approach the extreme of g(n) not contributing to f(n), and A* will degrade into Greedy Best-First-Search

### Diagnol distance (d)
```python
def diagnol_heuristic(self, start, goal):
        dx = abs(start[0] - goal[0])
        dy = abs(start[0] - goal[0])
        return min(dx, dy) * DIAGNOLCOST + (max(dx, dy) - min(dx, dy)) * HORIZONTALCOST
```
From the A* pages of Amit:
>Another way to write this is D * max(dx, dy) + (D2-D) * min(dx, dy). Patrick Lester writes it yet a different way, with if (dx > dy) (D * (dx-dy) + D2 * dy) else (D * (dy-dx) + D2 * dx). These are all equivalent.

## References

- [Amit's A* pages](http://theory.stanford.edu/~amitp/GameProgramming/)
- [Nicholas Swift's blog on A* search](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2)
- [Vaidehi Joshi's basecs blog on Depth-First search](https://medium.com/basecs/demystifying-depth-first-search-a7c14cccf056)
- [Vaidehi Joshi's basecs blog on Breadth-First search](https://medium.com/basecs/breaking-down-breadth-first-search-cebe696709d9)
<br><br>

> Note: Nicholas Swift's way of calculating the heuristic cost does not yield a good path and explores more number of unnessesary nodes as he overestimates the cost and the algorithm degrades into Greedy Best-First Search. Refer [this](http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#euclidean-distance-squared) page to get an idea on how to calculate the heuristic cost and the different ways of calculating it.

## License

[MIT](LICENSE) LICENSE