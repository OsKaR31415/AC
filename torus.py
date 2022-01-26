from random import randint, choice
from BoolGrid import BoolGrid
from grid_printer import *
from os import get_terminal_size
from time import sleep, time



def main():
    width, height = (get_terminal_size().columns)//2, get_terminal_size().lines-1
    grid = BoolGrid(width, height)
    printer = GridPrinter()
    grid.randomize()

    generation = 0
    while True:
        current = time()
        while time() - current < 0.1:
            generation += 1
            x, y = randint(0, grid.get_width()), randint(0, grid.get_height())
            x, y = x%grid.get_width(), y%grid.get_height()
            grid[y][x] = choice(grid.neighbours(x, y, 2))
        printer.title = f" generation: {generation} "
        printer(grid)
        # print(grid, end="\r")
        if grid.all_equal():
            return


main()


