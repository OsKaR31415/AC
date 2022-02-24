import curses
from time import sleep

class GridPrinter:
    __SYMBOL = {0: "  ",
                1: "░░",
                2: "▒▒",
                3: "▓▓",
                4: "██",
                False: "  ",
                True:  "██",}

    title = ""

    def __init__(self, delay: float =0, wait: bool =False):
        """
        Args:
            delay (float): The delay in seconds after each screen update.
            wait (bool): Whether to wait after each or not. If set to True, there is no delay anymore.
        """
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)  # hide cursor
        self.stdscr.keypad(True)

        # delay after a screen update
        self.__delay = float(delay)
        # wether to wait after each screen update or not
        self.__wait = bool(wait)
        if self.__wait:  # if you wait, there is no delay
            self.__delay = 0

    def terminate(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        curses.curs_set(1)  # show the cursor again

    def getkey(self):
        return self.stdscr.getkey()

    def __call__(self, grid):
        self.stdscr.erase()
        for y in range(grid.get_height()):
            for x in range(grid.get_width()):
                current_cell = grid[y][x]
                if not current_cell:
                    continue
                self.stdscr.addstr(y, x*2,
                        self.__SYMBOL[current_cell])
        self.stdscr.addstr(0, 0, str(self.title))
        self.stdscr.refresh()
        if self.__wait:
            self.stdscr.getkey()
        else:
            sleep(self.__delay)

    def update_cell(self, x: int, y: int, grid):
        self.stdscr.addstr(y, x*2, self.__SYMBOL[grid[y][x]])
        self.stdscr.refresh()

    def change_from_precedent(self, new_grid, precedent_grid) -> None:
        for y in range(new_grid.get_height()):
            for x in range(new_grid.get_width()):
                if new_grid[y][x] != precedent_grid[y][x]:
                    self.stdscr.addstr(y, x*2, self.__SYMBOL[new_grid[y][x]])
        self.stdscr.refresh()
        if self.__wait:
            self.stdscr.getkey()
        else:
            sleep(self.__delay)


