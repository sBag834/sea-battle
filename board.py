
class Board:
    def __init__(self, hid=False):
        self.list_dot = []     # список занятых точек
        self.list_ships = []   # список кораблей
        self.hid = hid         # видимость поля
        self.ships_dead = 0    # количество подбитых кораблей
        self.size = 6          # размер поля
        self.board = [["O"] * self.size for _ in range(self.size)]   # доска

    def add_ship(self, ship):
        for d in ship.ships_dots:
            if self.out(d) or d in self.list_dot:
                raise ValueError("В этом месте нельзя разместить корабль")

        for d in ship.ships_dots:
            self.board[d[0]][d[1]] = "■"
            self.list_dot.append(d)

        self.list_ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.ships_dots:
            for dx, dy in near:
                current = (d[0] + dx, d[1] + dy)
                if not self.out(current) and current not in self.list_dot:
                    if verb:
                        self.board[current[1]][current[0]] = "."
                    self.list_dot.append(current)

    def out(self, d):
        return not ((0 <= d[0] < self.size) and (0 <= d[1] < self.size))

    def shot(self, d):
        if self.out(d):
            raise ValueError("Выстрел за пределы доски")

        if d in self.list_dot:
            raise ValueError("В эту клетку уже стреляли")

        self.list_dot.append(d)

        for ship in self.list_ships:
            if ship.hit(d):
                ship.heart -= 1
                self.board[d[1]][d[0]] = "X"
                if ship.heart == 0:
                    self.ships_dead += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return True
                else:
                    print("Корабль подбит!")
                    return True

        self.board[d[1]][d[0]] = "T"
        print("Мимо!")
        return False

    def begin(self):
        self.list_dot = []

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.board):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def defeat(self):
        return self.ships_dead == len(self.list_ships)