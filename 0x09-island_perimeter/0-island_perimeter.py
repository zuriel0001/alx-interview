#!/usr/bin/python3
"""
Script to determine the perimeter of an island in grid.
"""


def island_perimeter(grid):
    """Return the perimiter of an island.

    The isaland grid is covered with land & water.
    represented by 1 and 0 respectively

    Args:
        grid (list): A list of list of integers representing the island.

    Returns:
        The perimeter of the island defined in grid.
    """

    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1

    return (size * 4 - edges * 2)
