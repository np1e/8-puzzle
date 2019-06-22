import numpy as np
from search import Search, Algorithm
import argparse
import datetime

class Puzzle:

    def __init__(self):
        self.start = np.array([[2, 8, 3],
                               [1, 6, 4],
                               [7, 0, 5]])
        #self.start = np.array([[1, 8, 7],
        #                       [2, 0, 6],
        #                       [3, 4, 5]])
        self.zero = (2,1)
        self.goal = np.array([[1, 2, 3],
                              [8, 0, 4],
                              [7, 6, 5]])

        self.size = len(self.start)

        self.moves = ["U", "D", "R", "L"]

        self.puzzle = self.start

    def __eq__(self, other):
        return (self.puzzle == other.puzzle).all()

    def checkPuzzle(self):
        return (self.puzzle == self.goal).all()

    def makeMoves(self, moves):
        for m in moves:
            self.move(m)

    def move(self, direction):
        if direction == "U":
            self.moveSpaceUp()
        if direction == "D":
            self.moveSpaceDown()
        if direction == "R":
            self.moveSpaceRight()
        if direction == "L":
            self.moveSpaceLeft()

    def swap(self, *points):
        x1, y1, x2, y2 = points
        self.puzzle[x1][y1], self.puzzle[x2][y2] = self.puzzle[x2][y2], self.puzzle[x1][y1]

    def moveSpaceUp(self):
        if self.zero[0] != 0:
            self.swap(self.zero[0]-1, self.zero[1], *self.zero)
            self.zero = (self.zero[0]-1, self.zero[1])

    def moveSpaceDown(self):
        if self.zero[0] != self.size-1:
            self.swap(self.zero[0]+1, self.zero[1], *self.zero)
            self.zero = (self.zero[0]+1, self.zero[1])

    def moveSpaceLeft(self):
        if self.zero[1] != 0:
            self.swap(self.zero[0], self.zero[1]-1, *self.zero)
            self.zero = (self.zero[0], self.zero[1]-1)

    def moveSpaceRight(self):
        if self.zero[1] != self.size-1:
            self.swap(self.zero[0], self.zero[1]+1, *self.zero)
            self.zero = (self.zero[0], self.zero[1]+1)

    def getState(self):
        return self.puzzle

    def expand(self):
        pass

    def __str__(self):
        string = ""
        for i in range(0, self.size):
            for j in range(0, self.size):
                string += str(self.puzzle[i][j]) + " | "
            string += "\n"
            string += "-"*4*self.size + "\n"

        return string

def play_puzzle(puzzle):
    move = ""
    moves = []
    print("Quit by typing \'q\'.")
    print("Make your moves by typing \'u\', \'d\', \'r\', \'l\'.")
    print("Have fun!\n")
    while not puzzle.checkPuzzle() and move != "q" :

        print(puzzle)
        move = input("Make your move (l, r, u, d): ")
        print("\n")
        if move == "l":
            puzzle.moveSpaceLeft()
        if move == "r":
            puzzle.moveSpaceRight()
        if move == "u":
            puzzle.moveSpaceUp()
        if move == "d":
            puzzle.moveSpaceDown()
        moves.append(move.upper())

    if move != 'q':
        print("Congratulations! You solved the puzzle with the following moves:")
        print(moves)
    else:
        print("Try again next time!")

def compare(search):
    print("A* algorithm with manhattan distance:")
    search.doAlgorithm(Algorithm.a_star, "m", False)
    print("\nA* algorithm with n wrong tiles:")
    search.doAlgorithm(Algorithm.a_star, "n", False)
    print("\nBreadth first algorithm:")
    search.doAlgorithm(Algorithm.breadth_first, False)
    print("\nDepth first with 15 max depth:")
    search.doAlgorithm(Algorithm.depth_first, 15, False)
    print("\nDepth first with max depth 10:")
    search.doAlgorithm(Algorithm.depth_first, 10, False)
    print("\nIterative deepening:")
    search.doAlgorithm(Algorithm.iter_deepening, False)

def main():

    parser = argparse.ArgumentParser(description="Play or let play an 8-Puzzle.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--p', action='store_true', help='lets you play the 8-puzzle')
    group.add_argument('-m', dest='moves', help='give the moves you want to execute as command line argument')
    group.add_argument('--d', dest='depth_first', action='store_true',
                       help='search for a solution using the depth first algorithm')
    group.add_argument('--di', dest='iterative_depth_first', action='store_true',
                       help='search for a solution using the depth first algorithm with iterative deepening')
    group.add_argument('-d', dest='max_depth_first', metavar='MAX DEPTH', type=int,
                       help='search for a solution using the depth first algorithm with a maximum depth')
    group.add_argument('--b', dest='breadth_first', action='store_true',
                        help='search for a solution using the breadth first algorithm')
    group.add_argument('-a', dest='a_star', metavar='HEURISTIC', type=str,
                       help='search for solution using the A* algorithm with \'m\' for manhattan distance as heuristic and \'n\' for n wrong tiles as heuristic')
    group.add_argument('--c', dest='compare', action='store_true',
                       help='compares all algorithms')

    puzzle = Puzzle()
    search = Search(puzzle)

    args = parser.parse_args()

    if args.p:
        play_puzzle(puzzle)
    elif args.moves:
        puzzle.makeMoves(args.moves)
        print(puzzle)
        if puzzle.checkPuzzle():
            print("Congratulations! You solved the puzzle!")
    elif args.iterative_depth_first:
        search.doAlgorithm(Algorithm.iter_deepening)
    elif args.max_depth_first:
        search.doAlgorithm(Algorithm.depth_first, args.max_depth_first)
    elif args.depth_first:
        search.doAlgorithm(Algorithm.depth_first)
    elif args.breadth_first:
        search.doAlgorithm(Algorithm.breadth_first)
    elif args.a_star:
        search.doAlgorithm(Algorithm.a_star, args.a_star)
    elif args.compare:
        compare(search)



if __name__ == "__main__":
    main()