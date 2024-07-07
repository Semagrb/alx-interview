N Queens Problem
================

This is a solution to the N Queens problem, which is a classic problem in computer science and mathematics. The problem is to place N queens on an NxN chessboard such that no queen attacks another.

Usage
-----

To use this program, simply run it from the command line and pass the size of the chessboard as an argument. For example:
./0-nqueens.py 4
This will print all possible solutions to the 4 queens problem.

Requirements
------------

* The program must be run from the command line.
* The program must take a single argument, which is the size of the chessboard.
* The program must print all possible solutions to the N queens problem.
* Each solution must be printed on a separate line.
* The format of each solution is a list of lists, where each inner list represents a queen's position on the board.
* The program must handle invalid input, such as non-numeric arguments or arguments less than 4.

Implementation
--------------

This program uses a backtracking approach to solve the N queens problem. It recursively tries to place queens on the board, and uses a helper function to check if a given position is safe for a queen.
