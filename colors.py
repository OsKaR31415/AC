
class Color:
    reset = "\u001b[0m"
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"
    reset = "\u001b[0m"

    teal = "\u001b[38;5;6m"

    def code(self, code) -> str:
        return "\u001b[38;5;" + str(code) + "m"

    def __call__(self, value: int or str, string: str) -> str:
        if isinstance(value, str):
            return getattr(self, value) + str(string) + self.reset
        if isinstance(value, int):
            return self.code(value) + str(string) + self.reset

    def grey(self, level: float, string: str) -> str:
        """Make a grey background escape sequence from a grey level.
        The grey level is exprimed as a float between 0 and 1."""
        level = abs(level)
        level = min(level, 1)
        # [0; 1] --> int([232; 255])
        colorcode = int(232 + (level * 23))
        return self(colorcode, string)




