from secrets import choice
from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
import sys


class Game:
    def __init__(self):
        self.banker = Banker()
        self.dice_quantity = 6
        self.rounds = 0
        self.status = True
        
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

    def game_handler(self, roller):
        rolled_dice = self.roll(roller)
        selected_dice = self.validate_dice(rolled_dice, roller)
        self.compile_score(selected_dice)
        self.score_and_dice_quantity()
        self.bank_reroll_quit(roller)

    def quit_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def start_round(self, roller):
        self.rounds += 1
        self.dice_quantity= 6
        self.banker.clear_shelf()
        print(f"Starting round {self.rounds}")
        self.game_handler(roller)

    def roll(self, roller):
        print(f"Rolling {self.dice_quantity} dice...")
        roll = roller(self.dice_quantity)
        self.show_dice_rolled(roll)
        return roll

    def show_dice_rolled(self, roller):
        roll = roller(self.dice_quantity)
        roller_str = ''
        for num in roll:
            roller_str += str(num) + " "
        print(f'*** {roller_str}***')

    def validate_dice(self, rolled_dice, roller):
        if GameLogic.calculate_score(rolled_dice) == 0:
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")
            self.banker.clear_shelf()
            self.bank_earned_points()
        else:
            print("Enter dice to keep or (q)uit:")
            response = input(">")
            if response:
                response = response.replace(" ", "")
            else: self.validate_dice(rolled_dice, roller)
        if response == "q":
            self.quit_game()
        while True:
            keeper_values =[]
            for char in response:
                    if char():
                        keeper_values.append(int(char))
            if GameLogic.validate_keepers(rolled_dice, keeper_values):
                    return keeper_values
            else: 
                print("Cheater!!! Or possibly made a typo...")
            return self.validate_dice(rolled_dice, roller)
    def compile_score(self, user_response):
        user_response = tuple(map(int, list(choice)))
        self.dice_quantity -= len(user_response)
        score = GameLogic.calculate_score(user_response)
        self.banker.shelf(score)
        return score



    def score_and_dice_quantity(self):
        print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining") 

    def bank_reroll_quit(self,roller):

        print("(r)oll again, (b)ank your points or (q)uit:")
        response = input("> ").replace(" ", "")

        if response == "q":
            self.quit_game()

        elif response == "r":
            if self.dice_quantity == 0:
                self.dice_quantity = 6
                self.game_handler(roller)
            else:
                self.game_handler(roller)

        elif response == "b":
            self.bank_earned_points()

    def bank_earned_points(self, roller):
        print(f"You banked {self.banker.shelved} points in round {self.rounds}")
        self.banker.bank()
        print(f"Total score is {self.banker.balance} points")        
        if self.banker.balance >= 10000:
            print("WINNER")
        else:
            self.start_round(roller)   


    # def start_round(self, roller):

    #     while self.status and self.banker.balance <= 1000:
    #         self.rounds += 1
    #         print(f"Starting round {self.rounds}")
    #         print(f"Rolling {self.dice_quantity} dice...")
    #         roll = roller(self.dice_quantity)
    #         # roller_str = " ".join(map(str, roll))
    #         roller_str = ""
    #         for num in roll:
    #             roller_str += str(num) + " "
    #         print(f"*** {roller_str} ***")
    #         print(f"Enter dice to keep, or (q)uit:")
    #         response = input("> ")

    #         if response == "q":
    #             print(f"Thanks for playing. You earned {self.banker.balance} points")
    #             sys.exit()
    #         else:
    #             user_response = tuple(map(int, list(response)))
    #             self.dice_quantity -= len(user_response)
    #             score = GameLogic.calculate_score(user_response)
    #             self.banker.shelf(score)
    #             print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")
    #             print(f"(r)oll again, (b)ank your points or (q)uit:")
    #             response = input("> ")

    #         if response == "b":
    #             self.banker.bank()
    #             self.dice_quantity = 6
    #             print(f"You banked {score} points in round {self.rounds}")
    #             print(f"Total score is {self.banker.balance} points")

    #         elif response == "r":
    #             if self.dice_quantity == 0:
    #                 self.dice_quantity = 6
    #                 continue

    #         elif response == "q":
    #             print(f"Thanks for playing. You earned {self.banker.balance} points")
    #             sys.exit()


if __name__ == "__main__":
    game = Game()
    game.play()
