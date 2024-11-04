import random

from board import Board
from ship import Ships

class Game:
    def __init__(self):
        player_board = self.random_board()
        ai_board = self.random_board()
        ai_board.hid = True

        self.player = player_board
        self.ai = ai_board
        self.ai_turns = []

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        board = Board()
        trying = 0
        for size_ship in [3,2,2,1,1,1,1]:
            while True:
                trying += 1
                if trying > 2000:
                    return None
                ship = Ships(size_ship,(random.randint(0,5), random.randint(0,5)), random.randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except ValueError:
                    pass
        board.begin()
        return board

    def great(self):
        print("=====Приветствую вас и игре 'Морской бой'!=====")
        print("              Формат ввода: x y                ")
        print("")
        print("  х - номер столбца         у - номер строчки  ")

    def user_move(self):
        while True:
            cord = input("Ваш ход: ").split()
            if len(cord) != 2:
                print("Введите две координаты!")
                continue

            x, y = cord

            if not (x.isdigit()) or not  (y.isdigit()):
                print("Введите числа!")
                continue

            x, y = int(x)-1, int(y)-1

            try:
                repeat = self.ai.shot((x,y))
                return repeat
            except ValueError as e:
                print(e)

    def ai_move(self):
        while True:
            x, y = random.randint(0,5), random.randint(0,5)
            if (x, y) not in self.ai_turns:
                if (x, y) not in self.player.list_dot:
                    self.ai_turns.append((x, y))
                    print(f'AI стреляет в {x+1} {y+1}')
                    repeat = self.player.shot((x, y))
                    return repeat

    def loop(self):
        num = 0
        while True:
            print("="*47)
            print("        Доска игрока")
            print("")
            print(self.player)
            print("")
            print("="*47)
            print("        Доска AI")
            print("")
            print(self.ai)
            print("")
            print("="*47)

            if num % 2 == 0:
                print("Ходит игрок")
                repeat = self.user_move()
            else:
                print("Ходит AI")
                repeat = self.ai_move()

            if repeat:
                num -= 1

            if self.ai.defeat():
                print("="*47)
                print("Игрок победил")
                break

            if self.player.defeat():
                print("="*47)
                print("AI победил")
                break
            num += 1