from queue import Queue
from copy import deepcopy

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


    def succ(self):
        succs = Queue()
        for m in self.state.moves:
            p = deepcopy(self.state)
            p.move(m)
            if p.zero is not self.state.zero:
                succs.put(Node(p, self, m))
        return succs


    def __str__(self):
        return str(self.moves)
