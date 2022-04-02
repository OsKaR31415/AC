from random import random
from time import sleep

SYMBOLS = {
        True: "██",
        False: "  "
        }

def random_bool(p: float = .5) -> bool:
    return p > random()

def game_of_life(neighbours: list[bool], current_cell: bool) -> bool:
    """The rule for the game of life."""
    neigh = sum(neighbours)
    if neigh == 3:
        return True
    if neigh == 2:
        return current_cell
    return False
    # return (neigh == 3) or (current_cell and neigh == 2)

def get_neighbours(grid: list[list[bool]], y: int, x: int) -> list[bool]:
    w, h = len(grid[0]), len(grid)
    return [grid[(y-1)%h][(x-1)%w], grid[(y-1)%h][x], grid[(y-1)%h][(x+1)%w],
            grid[(y  )%h][(x-1)%w],                   grid[y%h    ][(x+1)%w],
            grid[(y+1)%h][(x-1)%w], grid[(y+1)%h][x], grid[(y+1)%h][(x+1)%w]]

def apply_rule(rule, grid: list[list[bool]]) -> list[list[bool]]:
    width, height = len(grid[0]), len(grid)
    # empty grid of *grid*'s shape
    new_grid = [[None for _ in range(width)] for _ in range(height)]
    # loop on the cells
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            c = rule(get_neighbours(grid, y, x), cell)
            new_grid[y][x] = c
    return new_grid


def show(grid: list[list[bool]]) -> None:
    res = "\n\n"
    for line in grid:
        res += "\n"
        for elt in line:
            res += SYMBOLS[elt]
    print(res, end="")

def beamer_show(grid: list[list[bool]]) -> None:
    result = "\n\\def\\figureGrid{\n"
    for line in grid[:-1]:
        result += "    {"
        result += ','.join(map(lambda x: '01'[x], line))
        result += "},\n"
    result += '    {' + ','.join(map(lambda x: '01'[x], grid[-1])) + '}%\n'
    result += '}\\gridFrame{\\figureTitle}{\\figureGrid}\n'
    print(result)


def main():
    # WIDTH, HEIGHT = int(input("Enter width : ")), int(input("Enter height : "))
    WIDTH, HEIGHT = 37, 15
    generation = 0
    grid = [[random_bool(.3) for _ in range(WIDTH)] for _ in range(HEIGHT)]
    previous_grids = [grid]
    print("\\newcommand\\figureTitle{Evolution d'une grille aléatoire}\n")
    while grid not in previous_grids[:-1]:
        grid = apply_rule(game_of_life, grid)
        beamer_show(grid)
        previous_grids.append(grid)
        generation += 1
        # sleep(.01)
    print(generation, "generations")


if __name__ == "__main__":
    main()

