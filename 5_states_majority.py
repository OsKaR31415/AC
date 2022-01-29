from random import randint, choice
from BoolGrid import *
from collections import Counter
from os import get_terminal_size
from time import sleep, time



def rule(cell: int, neighbours: list[int]) -> bool:
    """Returns the rule depending on the neighbours of a given cell and of the
    state of this cell."""
    neighbours = Counter(neighbours)
    neighbours.update(cell)
    return neighbours.most_common(1)[0][0]


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




