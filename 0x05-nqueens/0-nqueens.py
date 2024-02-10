#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def solve(row, size, columns, positive, negative, grid):
    """
    solve function to find solution
    """
    if row == size:
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result.append([i, j])
        print(result)
        return

    for col in range(size):
        if (col in columns or
            (row + col) in positive or
            (row - col) in negative):
            continue

        columns.add(col)
        positive.add(row + col)
        negative.add(row - col)
        grid[row][col] = 1

        solve(row+1, size, columns, positive, negative, grid)

        columns.remove(col)
        positive.remove(row + col)
        negative.remove(row - col)
        grid[row][col] = 0


def nqueens(size):
    """
    Method to solve to nqueens problem
    Args:
        size (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    columns = set()
    positive_diag = set()
    negative_diag = set()
    grid = [[0] * size for i in range(size)]

    solve(0, size, columns, positive_diag, negative_diag, grid)


if __name__ == "__main__":
    size = sys.argv
    if len(size) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(size[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
