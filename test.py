#кораблики - ■
#промазал - T
#попал - X


letters = ("A", "B", "C", "D", "E", "F")
ships_rules = [1, 1, 1, 1, 2, 2, 3]
field_size = len(letters)

class Internal_logic:

    class Dot:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

    class Ships:
        def __init__(self, size_ship, point_ship, orient, heart):
            self.size_ship = size_ship
            self.point_ship = point_ship
            self.orient = orient
            self.heart = heart

        def dots(self):
            return

    class Board:
        def __init__(self, list_dot, list_ships, hid, ships_live, size):
            self.list_dot = list_dot
            self.list_ships = list_ships
            self.hid = hid
            self.shops_live = ships_live
            self.size = size

        def add_ship(self):
            pass

        def contour(self):
            pass

        @property
        def print_board(self): #выводит доску в зависимости от значения hit
            for x in range(-1, self.size):
                for y in range(-1, self.size):
                    if x == -1 and y == -1:
                        print("  ", end="")
                        continue
                    if x == -1 and y >= 0:
                        print(y + 1, end=" ")
                        continue
                    if x >= 0 and y == -1:
                        print(letters[x], end='')
                        continue
                    print(" " + str("O"), end='')
                print("")

        def out(self):
            pass

        def shot(self):
            pass

class External_logic:
    class Player:
        def __init__(self, you_board, enemy_board):
            self.you_board = you_board
            self.enemy_board = enemy_board

        def ask(self):
            pass

        def move(self):
            pass

    class AI(Player):

        def ask(self):
            pass

    class User(Player):

        def ask(self):
            pass

class Game:
    def __init__(self):
        pass

    def random_board(self):
        pass

    def greet(self):
        pass

    def loop(self):
        pass

    def start(self):
        pass


a = Internal_logic.Board(1,1,2,3,6).print_board
print(a)