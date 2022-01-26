
class Figure:
    def __init__(self, coords: list[int]):
        self.coords = list(coords)
        min_coord_x = min(map(lambda c: c[0], self.coords))
        min_coord_y = min(map(lambda c: c[1], self.coords))
        max_coord_x = max(map(lambda c: c[0], self.coords))
        max_coord_y = max(map(lambda c: c[1], self.coords))
        self.width = max_coord_x - max_coord_x
        self.height = max_coord_y - min_coord_y



# period 2 :

blinker = [(0, 0), (0, 1), (0, 2)]

barber_pole = [(0, 0), (0, 1), (1, 0), (2, 1), (2, 3), (4, 3), (4, 5), (5, 6), (6, 6), (6, 5)]

block = [(0, 0), (0, 1), (1, 0), (1, 1)]

glider = [(0, 2), (1, 0), (1, 2), (2, 1), (2, 2)]

