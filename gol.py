from random import randint, choice
from BoolGrid import import BoolGrid
from grid_printer import *
import gol_figures
from os import get_terminal_size
from time import sleep, time


def rule(cell: bool, neighbours: list[bool]) -> bool:
    """Returns the rule depending on the neighbours of a given cell and of the
    state of this cell."""
    neighbours = sum(neighbours)
    return neighbours == 3 or cell and neighbours == 2

def next_grid(grid: BoolGrid) -> BoolGrid:
    new_grid = BoolGrid(grid.get_width(), grid.get_height())
    for y in range(grid.get_height()):
        for x in range(grid.get_width()):
            new_grid[y][x] = rule(grid[y][x], grid.neighbours(x, y))
    return new_grid

def main():
    # width, height = (get_terminal_size().columns-2)//2, get_terminal_size().lines-4
    width, height = (get_terminal_size().columns-2)//2, get_terminal_size().lines
    grid = BoolGrid(width, height)
    printer = GridPrinter()

    # ''' comment this line to randomize the grid
    grid.randomize(.3)
    '''
    grid.set(gol_figures.barber_pole, at=(1, 1))
    grid.set(gol_figures.block, at=(8, 1))
    grid.set(gol_figures.glider, at=(12, 1))
    grid.set(gol_figures.blinker, at=(2, 8))
    # '''

    try:
        generation = 0
        # variable to remember previous grids
        previous_grids = [None]*20  # 20 so 20 grids are stored
        while grid not in previous_grids:
            time_stamp = time()
            while time() - time_stamp < 0.5:
                grid_before_screen_update = grid
                generation += 1
                # change the remembered grids (remove the oldest one and append
                # the current one)
                previous_grids.pop(0)
                previous_grids.append(grid)
                # update the grid
                grid = next_grid(grid)
                # sleep(.05)
                printer.title = f"gen: {generation}"
                printer.change_from_precedent(grid, grid_before_screen_update)
            # printer(grid)
        printer.getkey()
    except KeyboardInterrupt:
        printer.getkey()
        printer.terminate()
    # '''


main()


