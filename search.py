from datetime import datetime
import node
from queue import Queue, LifoQueue, PriorityQueue
from enum import Enum
from itertools import count

class Algorithm(Enum):
    depth_first = 0
    breadth_first = 1
    iter_deepening = 2
    a_star = 3

class Search():

    def __init__(self, puzzle):
        self.start = node.Node(puzzle)

    def doAlgorithm(self, algorithm, *args):
        startTime = datetime.now()
        if algorithm == Algorithm.depth_first:
            if args:
                result = self.depthFirst(*args)
            else:
                result = self.depthFirst(*args)
        elif algorithm == Algorithm.breadth_first:
            result = self.breadthFirst(*args)
        elif algorithm == Algorithm.iter_deepening:
            result = self.iterativeDeepening(*args)
        elif algorithm == Algorithm.a_star:
            result = self.a_search(*args)

        endTime = datetime.now()
        diff = endTime-startTime
        print(f"Algorithm took {diff} to return with result {result}")
        return diff, result

    def breadthFirst(self, verbose = True):
        queue = Queue()
        queue.put(self.start)
        reached = []
        while queue:
            node = queue.get()
            if verbose:
                print(f"Current node: {str(node)}")
            if node.isGoal():
                return node
            elif not node.isIn(reached):
                reached.append(node)
                succs = node.succ()
                for s in succs.queue:
                    queue.put(s)
        return None

    def iterativeDeepening(self, verbose = True):
        depth = 1
        result = None
        while result is None:
            result = self.depthFirst(depth, verbose)
            depth += 1
        return result

    def depthFirst(self, max_depth = 15, verbose = True):
        queue = LifoQueue()
        queue.put(self.start)
        reached = []
        while not queue.empty():
            node = queue.get()
            if verbose:
                print(f"Current node: {str(node)}")
            if node.isGoal():
                return node
            elif node.depth != max_depth and not node.isIn(reached):
                reached.append(node)
                succs = node.succ()
                while not succs.empty():
                    queue.put(succs.get())

        return None



    def a_search(self, heuristic, verbose= True):
        counter = count()
        queue = PriorityQueue()
        queue.put((self.start.heur(heuristic), next(counter), self.start))
        reached = []

        while not queue.empty():
            node = queue.get()[2]
            if verbose:
                print(f"Current node: {str(node)}")
            if node.isGoal():
                return node
            elif not node.isIn(reached):
                reached.append(node)
                succs = node.succ()
                while not succs.empty():
                    child = succs.get()
                    queue.put((child.heur(heuristic) + child.cost(), next(counter), child))
        return None




