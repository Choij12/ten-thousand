from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
import sys


class Game:
    def __init__(self):
        self.banker = Banker()
        self.dice_quantity = 6
        self.rounds = 0
        self.status = True

    # def play(self, roller=GameLogic.roll_dice):
    def default_roller(self):
        GameLogic.roll_dice(self.dice_quantity)

    def play(self, roller=GameLogic.roll_dice):
        self.default_roller = roller
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        while True:
            response = input("> ")
            if response == "n":
                print("OK. Maybe another time")
                break
            elif response == "y":
                self.start_round(roller)

    def start_round(self, roller):

        while self.status and self.banker.balance <= 1000:
            self.rounds += 1
            print(f"Starting round {self.rounds}")
            print(f"Rolling {self.dice_quantity} dice...")
            roll = roller(self.dice_quantity)
            roller_str = " ".join(map(str, roll))
            print(f"*** {roller_str} ***")
            print(f"Enter dice to keep, or (q)uit:")
            response = input("> ")

            if response == "q":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                sys.exit()
            else:
                user_response = tuple(map(int, list(response)))

                self.dice_quantity -= len(user_response)
                score = GameLogic.calculate_score(user_response)
                self.banker.shelf(score)
                print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")
                print(f"(r)oll again, (b)ank your points or (q)uit:")
                response = input("> ")

            if response == "b":
                self.banker.bank()
                self.dice_quantity = 6
                print(f"You banked {score} points in round {self.rounds}")
                print(f"Total score is {self.banker.balance} points")

            elif response == "r":
                if self.dice_quantity == 0:
                    self.dice_quantity = 6
                    continue

            elif response == "q":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                sys.exit()


if __name__ == "__main__":
    game = Game()
    game.play()
