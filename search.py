from datetime import datetime
import node
from queue import Queue, LifoQueue
from enum import Enum


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
                result = self.depthFirst()
        elif algorithm == Algorithm.breadth_first:
            result = self.breadthFirst()
        elif algorithm == Algorithm.iter_deepening:
            result = self.iterativeDeepening()
        elif algorithm == Algorithm.a_star:
            result = self.a_search()

        endTime = datetime.now()
        diff = endTime-startTime
        print(f"Algorithm took {diff} to return with result {result}")

    def breadthFirst(self):
        queue = Queue()
        queue.put(self.start)
        reached = []
        while queue:
            node = queue.get()
            #print(f"Current node: {str(node)}")
            if node.isGoal():
                return node
            elif not node.isIn(reached):
                reached.append(node)
                succs = node.succ()
                for s in succs.queue:
                    queue.put(s)
        return None

    def iterativeDeepening(self):
        depth = 1
        result = None
        while result is None:
            result = self.depthFirst(depth)
            depth += 1
        return result

    def depthFirst(self, max_depth = 15):
        queue = LifoQueue()
        queue.put(self.start)
        reached = []
        while queue:
            if queue.empty():
                return None
            node = queue.get()
            print(f"Current node: {str(node)}")
            if node.isGoal():
                return node
            elif node.depth != max_depth and not node.isIn(reached):
                reached.append(node)
                succs = node.succ()
                while not succs.empty():
                    queue.put(succs.get())

        return None


    def a_search(self):
        pass



