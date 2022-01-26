from random import random
from grid_printer import GridPrinter
from time import sleep


class Grid:
    """
    Attributes:
        title (str): The string to show at the top of the grid. (maybe the time
                     spent of the number of step done).
    """

    __SYMBOL = {0: "  ",
                1: "░░",
                2: "▒▒",
                3: "▓▓",
                4: "██",
                False: " ",
                True:  "██",}

    def __init__(self, width: int, height: int, title: str =""):
        self.__width = int(width)
        self.__height = int(height)
        self.__grid = [[0 for _ in range(width)] for _ in range(height)]
        self.title = str(title)

    def fill(self, value: int):
        """Fills the grid with the given value.
        Args:
            value (int): The value to fill the grid with"""
        value = int(value)
        for y in range(self.__height):
            for x in range(self.__width):
                self.__grid[y][x] = value

    def randomize(self, value, probability: float =0.5) -> None:
        """Fill the grid with random values.
        Args:
            value: the value to fill the grid with
            probabilily (float): The probabilily of having a *value* cell.
                                 Default to 0.5
        """
        value = int(value)
        probability = float(probability)
        for y in range(self.__height):
            for x in range(self.__width):
                if random() < probability:
                    self.__grid[y][x] = value

    def get_grid(self) -> list[list[bool]]:
        """Get the boolean grid.
        Returns:
            list[list[bool]]: The representation of the grid as a list of lists
                              (an array) containing bools.
        """
        return self.__grid

    def get_width(self) -> int:
        """Get the width of the grid.
        Returns:
            int: The width of the grid (the number of lines).
        """
        return self.__width

    def get_height(self) -> int:
        """Get the height of the grid.
        Returns:
            int: The height of the grid (the number of columns).
        """
        return self.__height

    def all_equal_to(self, value: int) -> bool:
        """Test if the grid is all filled with *value*.
        Args:
            value: The value to test.
        Returns:
            bool: True if the grid is filled with only values equal to *value*.
        """
        value = int(value)
        for y in range(self.__height):
            for x in range(self.__width):
                if self.__grid[y][x] != value:
                    return False
        return True

    def all_equal(self) -> bool:
        """Test if the grid is filled with values that are all equal.
        Returns:
            bool: True if the grid is filled either with only True, or only False.
        """
        first_cell = self.__grid[0][0]
        for y in range(self.__height):
            for x in range(self.__width):
                if self.__grid[y][x] != first_cell:
                    return False
        return True

    def set_symbols(self, symbols: list[str]):
        """Set the symbols for the different states.
        Args:
            symbols (list[str]): The list of the symbols for each state. Each
                                 symbol should be a 2 caracter string.
        """
        dead = str(dead)[:2]
        alive = str(alive)[:2]
        self.__SYMBOL = [dead, alive]

    def __getitem__(self, index: int) -> list[bool]:
        """Magic function for the indexation of the grid.
        Returns the index'th line of the grid.
        Since this value is a list, you also can index it.
        """
        return self.__grid[index]

    def __eq__(self, other) -> bool:
        """Test if *self* is the same grid as *other*.
        """
        if not isinstance(other, Grid):
            return False
        if self.get_width() != other.get_width():
            return False
        if self.get_height() != other.get_height():
            return False
        for x in range(self.__width):
            for y in range(self.__height):
                if self[y][x] != other[y][x]:
                    return False
        return True

    def __get_symbol_for__(self, state: int) -> str:
        """Get the symbol for a given state.
        Args:
            state (int): The state you want to get the symbol for.
        Returns:
            str: The string that is used to represent the state *state*.
        """
        return self.__SYMBOL[state]

    def set(self, coords: list[tuple[int]],
            at: tuple[int] =(0, 0),
            value: int =1):
        """Set the cells at the given coordinates to the value *value*.
        The coordinates are shifted, as if they were starting at *at*.
        By default, they are not shifted, and the cells are set to True.
        """
        for coord in coords:
            x, y = coord
            x += at[0]
            y += at[1]
            self[y][x] = value

    def neighbours(self, x: int, y: int, degree: int =1) -> list[bool]:
        """Get the Moore neighbours of the cell at the position (x, y).
        The neighboorhood is at a degree of *degree*.
        Args:
            x (int): The x position of the cell you want the neighbours of.
            y (int): The y position of the cell you want the neighbours of.
            degree (int): The degree of the Moore neighboorhood. Default to 1.
        Returns:
            list[int]: The neighbours of the cell at the position (x, y) in
                        the grid, using the Moore neighboorhood at a degree of
                        *degree*.
        """
        neighbours = []
        for shift_y in range(-degree, degree+1):
            for shift_x in range(-degree, degree+1):
                if shift_y != 0 or shift_x != 0:
                    x_pos = (x+shift_x) % self.__width
                    y_pos = (y+shift_y) % self.__height
                    neighbours.append(self[y_pos][x_pos])
        return neighbours

    def __str__(self) -> str:
        result = "┏" + str(self.title).center(self.__width*2, "━") + "┓\n"
        for line in self.__grid:
            result += "┃" + ''.join(map(self.__get_symbol_for__, line)) + "┃\n"
        # The \r is so it does not make a blank line
        return result + "┗" + "━"*self.__width*2 + "┛"




if __name__ == "__main__":
    # initialize a grid
    grid = Grid(16, 10, title=" grid ")
    printer = GridPrinter(wait=True)
    grid.randomize(.3, 1)
    grid.randomize(.3, 2)
    printer(grid)


