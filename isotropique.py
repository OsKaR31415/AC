from grid_printer import GridPrinter
from random import random, randint
from time import sleep
from os import get_terminal_size
from os import system
from copy import deepcopy
from time import time
import curses

global generation
generation = 0

class Cell:
    def __init__(self, alive: bool, speed: tuple[int] =(0, 0)):
        self.alive = bool(alive)
        self.speed = (speed[0], speed[1])

    def new_position(self, x: int, y: int) -> tuple[int]:
        if not self.alive:
            return (x, y)
        return (x + self.speed[0], y + self.speed[1])

    def __str__(self):
        return "██" if self.alive else "  "

    def invert_speed(self):
        inverted = (-self.speed[0], -self.speed[1])
        self.speed = inverted

    def __repr__(self):
        return f"Cell({self.alive}, {self.speed})"

def random_bool(probability: float =.5):
    return random() < float(probability)

def random_speed(min_speed: int, max_speed: int):
    speed = (randint(min_speed, max_speed), randint(min_speed, max_speed))
    # the speed shouldn't be null
    if speed == (0, 0):
        return random_speed(min_speed, max_speed)
    return speed

def random_grid(width: int,
                height: int,
                probability: float =0.5) -> list[list[Cell]]:
    grid = [
            [
                Cell(random_bool(probability),
                     speed=(random_speed(-3, 4)))
                for _ in range(width)]
            for _ in range(height)]
    return grid

def aff_grid(stdscr, grid: list[list[Cell]]) -> None:
    global generation
    stdscr.clear()
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            stdscr.addstr(y, x*2, str(cell))
    stdscr.addstr(0, 0, str(generation))
    stdscr.refresh()

def update_cell(x: int, y: int, grid: list[list[Cell]]) -> list[list[Cell]]:
    new_y, new_x = (grid[y][x]).new_position(y, x)
    if new_y >= len(grid) or new_x >= len(grid[0]):
        return grid
    # if there is a collision, invert speed
    if grid[new_y][new_x].alive:
        grid[y][x].invert_speed()
    else:
        grid[new_y][new_x] = grid[y][x]
        grid[y][x] = Cell(False)
    return grid

def next_grid(grid: list[list[Cell]]) -> list[list[Cell]]:
    return update_cell(randint(0, len(grid[0])-1),
                       randint(0, len(grid)-1),
                       grid)
    # new_grid = grid
    # for y, line in enumerate(grid):
    #     for x, cell in enumerate(line):
    #         new_grid = update_cell(x, y, grid)
    # return new_grid

def main(stdscr):
    global generation
    width, height = get_terminal_size()
    width, height = width//2, height-1
    grid = random_grid(width, height, probability=.03)
    while True:
        previous_time = time()
        aff_grid(stdscr, grid)
        while time() - previous_time < 1:
            grid = next_grid(grid)
            generation += 1
            sleep(0.00001)
        # input()




if __name__ == "__main__":
    curses.wrapper(main)


