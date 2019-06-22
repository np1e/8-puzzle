from queue import Queue
from copy import deepcopy
import numpy as np

class Node():
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        if self.parent is None:
            self.depth = 0
            self.moves = move
        else:
            self.depth = self.parent.depth+1
            self.moves = self.parent.moves + move

    def isIn(self, sequence):
        for s in sequence:
            if (self.state == s.state).all():
                return True
        return False

    def isGoal(self):
        return self.state.checkPuzzle()

    def cost(self):
        return self.depth

    def succ(self):
        succs = Queue()
        for m in self.state.moves:
            p = deepcopy(self.state)
            p.move(m)
            if p.zero is not self.state.zero:
                succs.put(Node(p, self, m))
        return succs

    def heur(self, heuristic):
        return self.wrongTiles() if heuristic == 'n' else self.manhattanDistance()

    def manhattanDistance(self):
        distance = 0
        for i in range(1, self.state.size**2):
            curIndex = np.argwhere(self.state.puzzle == i)[0]
            goalIndex = np.argwhere(self.state.goal == i)[0]
            dist = sum([np.abs(a-b) for a,b in zip(curIndex, goalIndex)])
            distance += dist

        return distance

    def wrongTiles(self):
        n = 0
        for i in range(0, self.state.size):
            for j in range(0, self.state.size):
                if (i,j) != self.state.zero \
                        and self.state.puzzle[i][j] != self.state.goal[i][j]:
                    n +=1

        return n
        n = sum([1 for x in (self.state.puzzle == self.state.goal).flatten() if not x])


    def __str__(self):
        return str(self.moves)
