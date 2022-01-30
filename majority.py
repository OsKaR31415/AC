from random import randint, choice
from BoolGrid import BoolGrid
from grid_printer import GridPrinter
from os import get_terminal_size
from time import sleep, time


def rule(cell, neighbours):
    return True


# def next_grid(grid: BoolGrid) -> BoolGrid:
#     new_grid = BoolGrid(grid.get_width(), grid.get_height())
#     for y in range(grid.get_height()):
#         for x in range(grid.get_width()):
#             new_grid[y][x] = rule(grid[y][x], grid.neighbours(x, y, 1))
#     return new_grid


def main():
    width, height = (get_terminal_size().columns)//2, get_terminal_size().lines
    grid = BoolGrid(width, height)
    printer = GridPrinter()
    # ''' comment this line to randomize the grid
    grid.randomize()

    while True:
        time_stamp = time()
        while time() - time_stamp < 0.05:
            x, y = randint(0, grid.get_width()-1), randint(0, grid.get_height()-1)
            grid[y][x] = .5 > sum([grid[y][x]] + grid.neighbours(x, y, 2))/16
            # printer.update_cell(x, y, grid)
            # grid[y][x]= not grid[y][x]
        # printer(grid)
        # printer.getkey()
    # '''

main()
