
class CellularAutomaton:
    __generation = 0

    def __init__(self, grid, rule):
        self.__rule = rule
        self.__grid = grid

    def step(self):
        new_grid = self.__grid
        for x in range(self.__grid.get_width()):
            for y in range(self.__grid.get_height()):
                new_grid[y][x] = rule(grid[y][x], grid.neighbours(x, y))
        self.__grid = new_grid
        self.__generation += 1

    def get_generation(self):
        return self.__generation

    def __str__(self):
        return str(self.__grid)

