#!/usr/bin/python3
"""
An algorithm for island parameter
"""


def island_parameter(grid):
    """
    gets the perimeter of an island in a list
    """

    grid_length = len(grid)
    grid_width = len(grid[0])
    length_list = []
    width_list = []

    if not grid:
        return

    for y in range(0, grid_length):
        length = 0
        width = 0
        for x in range(0, grid_width):
            if grid[y][x] == 0:
                continue
            if grid[y][x] == 1:
                if not (grid[y][x - 1]):
                    width += 1
                if (grid[y][x - 1]) and (grid[y][x - 1] == 1):
                    width += 1
                if (grid[y][x - 1]) and (grid[y][x - 1] == 0):
                    if (grid[y][x - 2]) and (grid[y][x - 2] == 1):
                        width = 0
                        break
                    else:
                        width += 1
        if width != 0:
            length += 1
            length_list.append(length)
            width_list.append(width)
    return ((max(width_list) + sum(length_list)) * 2)
