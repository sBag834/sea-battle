from board import Board

class Ships:
    def __init__(self, size_ship, point_ship, orient):
        self.size_ship = size_ship
        self.point_ship = point_ship
        self.orient = orient
        self.heart = size_ship

    @property
    def ships_dots(self):
        dot_list_ship = []

        for i in range(self.size_ship):
            x = self.point_ship[0]
            y = self.point_ship[1]

            if self.orient == 0:
                x += i
            elif self.orient == 1:
                y += i

            dot_list_ship.append((x, y))
        return dot_list_ship

    def hit(self, shot):
        return shot in self.ships_dots