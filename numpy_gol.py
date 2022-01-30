import numpy as np
from random import random
from time import sleep, time
from os import system, get_terminal_size
import curses


@np.vectorize
def cell_to_str(cell: bool) -> str:
    return "██" if cell else "  "


def show_grid(stdscr, grid: list[list[bool]]) -> None:
    stdscr.clear()
    x, y = 0, 0
    width = len(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            stdscr.addstr(y, x*2, "██" if grid[y][x] else "  ")
            # stdscr.refresh()
    stdscr.refresh()


def show(grid: list[list[bool]]) -> None:
    system("clear")
    print('┏', '━━'*len(grid[0]), '┓', sep="")
    for line in grid:
        print('┃', end='')
        for cell in line:
            print(cell_to_str(cell), end="")
        print('┃')
    print('┗', "━━"*len(grid[0]), '┛', sep='')


def neighbours(grid: list[list[bool]]) -> list[list[bool]]:
    def left(x):
        return np.roll(x,  1, axis=1)
    def right(x):
        return np.roll(x, -1, axis=1)
    def up(x):
        return np.roll(x,  1, axis=0)
    def down(x):
        return np.roll(x, -1, axis=0)
    # left  = lambda x: np.roll(x,  1, axis=1)
    # right = lambda x: np.roll(x, -1, axis=1)
    # up    = lambda x: np.roll(x,  1, axis=0)
    # down  = lambda x: np.roll(x, -1, axis=0)
    return np.array([left(up(grid)),  up(grid),   right(up(grid)),
                     left(grid),                  right(grid),
                     left(down(grid)), down(grid), right(down(grid))])


def rule(grid: list[list[bool]]) -> bool:
    neigh = np.sum(neighbours(grid), axis=0)
    return np.logical_or(
            neigh == 3,
            np.logical_and(
                neigh == 2,
                grid
                )
            )


@np.vectorize
def random_bool(*args) -> bool:
    return random() < .3


def main(stdscr):
    WIDTH, HEIGHT = get_terminal_size()
    WIDTH = get_terminal_size().columns // 2 -1
    HEIGHT = get_terminal_size().lines
    grid = np.empty((HEIGHT, WIDTH), dtype=bool)
    grid = random_bool(grid)
    while True:
        previous_update_time = time()
        while time() - previous_update_time < 0.3:
            grid = rule(grid)
        show_grid(stdscr, grid)

if __name__ == "__main__":
    curses.wrapper(main)
    # main(None)


