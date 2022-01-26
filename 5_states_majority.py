from random import randint, choice
from BoolGrid import *
import gol_figures
from os import get_terminal_size
from time import sleep, time



def rule(cell: int, neighbours: list[int]) -> bool:
    """Returns the rule depending on the neighbours of a given cell and of the
    state of this cell."""
    neighbours = sum(neighbours)
    return neighbours == 3 or cell and neighbours == 2

