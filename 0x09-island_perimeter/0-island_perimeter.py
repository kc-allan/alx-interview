#!/usr/bin/python3
"""Module for island_perimeter"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid
    :param grid: list of list of integers
    :return: perimeter of the island
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cell = grid[row][col]
            if cell == 1:
                # Count border
                top = 0 if grid[row - 1][col] == 1 else 1
                bottom = 0 if grid[row + 1][col] == 1 else 1
                left = 0 if grid[row][col - 1] == 1 else 1
                right = 0 if grid[row][col + 1] == 1 else 1

                perimeter += top + bottom + left + right

    return perimeter
