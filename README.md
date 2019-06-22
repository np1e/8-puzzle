# 8 puzzle

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)
+ [TODO](#todo)

## About <a name = "about"></a>
Python 3 implementation of the 8 puzzle with several algorithms so solve it, e.g. A*, breadth first and iterative deepening.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

The only external library needed to run the project is [numpy](https://www.numpy.org/). On the commandline run the following: 

```
pip install numpy 
```

### Installing

Just clone the repository to your local machine and you're good to go.

With ssh:
```
git clone git@github.com:np1e/8-puzzle.git
```

With https:
```
git clone https://github.com/np1e/8-puzzle.git
```

Now you can just run the `8-puzzle.py` without any arguments and it will display the possible arguments.

## Usage <a name = "usage"></a>

There are several "modes" you can run the program in, use them as follows.
All of them use the same start and goal formation:

```
start:
2 | 8 | 3 | 
-----------
1 | 6 | 4 | 
-----------
7 | 0 | 5 | 
-----------
```

```
goal:
1 | 2 | 3 | 
-----------
8 | 0 | 4 | 
-----------
7 | 6 | 5 | 
-----------
```

### Play the game by yourself

When you run the program with the `--p` flag, you can try to solve the puzzle by yourself:

```
$ python3 8-puzzle.py
Quit by typing 'q'.
Make your moves by typing 'u', 'd', 'r', 'l'.
Have fun!

2 | 8 | 3 | 
------------
1 | 6 | 4 | 
------------
7 | 0 | 5 | 
------------

Make your move (l, r, u, d):
```

You can now move the empty tile, indicated by the zero, with the letters u, d, r, l followed by hitting the return key. The program ends when you solved the puzzle by reaching the goal state or when you typed q followed by return.

You can also use the `-m` flag followed by a sequence of moves and the moves will be executed and the resulting puzzle state printed:

```
$ python3 8-puzzle.py -m lludrl
2 | 8 | 3 | 
------------
1 | 6 | 4 | 
------------
0 | 7 | 5 | 
------------
```

### Depth-first search


DFS with maximum depth of 15:
```
$ python3 8-puzzle.py --d
```

DFS with maximum depth of choice:
```
$ python3 8-puzzle.py --d 10
```

Iterative deepening:
```
$ python3 8-puzzle.py --di
```

### Breadth-first search

```
$ python3 8-puzzle.py --b
```

### A* search

A* search with manhatten distance as heuristic:
```
$ python3 8-puzzle.py -a m
```

A* search with n wrong tiles as heuristic:
```
$ python3 8-puzzle.py -a n
```

### Comparison of all algorithms

```
$ python3 8-puzzle.py --c
A* algorithm with manhattan distance:
Algorithm took 0:00:00.003377 to return with result UULDR

A* algorithm with n wrong tiles:
Algorithm took 0:00:00.001001 to return with result UULDR

Breadth first algorithm:
Algorithm took 0:00:00.006652 to return with result UULDR

Depth first with 15 max depth:
Algorithm took 0:00:03.626600 to return with result RULLURDLURDRDLU

Depth first with max depth 10:
Algorithm took 0:00:00.287740 to return with result ULURDLURD

Iterative deepening:
Algorithm took 0:00:00.011360 to return with result UULDR
```

## TODO <a name="todo"></a>

---
- [ ] random start state
- [ ] own start state
- [ ] own goal state
