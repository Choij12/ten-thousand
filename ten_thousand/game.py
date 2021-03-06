from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
import sys

class Game:
    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.dice_quantity = 6
        self.rounds = 0
        self.status = True
        self.playing = True
        self.kept_dice = ()
        self.num_rounds = num_rounds

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

    # def end_game(self):
    #     print(f"Thanks for playing. You earned {self.banker.balance} points")
    #     sys.exit()


    def bank_earned_points(self, roller):
        print(f"You banked {self.banker.shelved} points in round {self.rounds}")
        self.banker.bank()
        print(f"Total score is {self.banker.balance} points")
        if self.banker.balance >= 1000:
            print("WINNER")
        else:
            self.start_round(roller)

    def is_zilch(self, roll):
        return GameLogic.calculate_score(roll) == 0

    def do_zilch(self):
        self.banker.clear_shelf()
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        print(f"You banked {self.banker.shelved} points in round {self.rounds}")
        print(f"Total score is {self.banker.balance} points")
        
        
        
        
        
        
        
    
    def collect_keepers(self, roll):
        keeper_values = self.validate_keepers(roll)
        points_for_current_roll = GameLogic.calculate_score(keeper_values)
        self.banker.shelf(points_for_current_roll)
        return keeper_values

    def validate_keepers(self, roll):
        while True:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "q":
                self.end_game()

            keeper_values = []
            for char in response:
                if char.isnumeric():
                    keeper_values.append(int(char))

            if GameLogic.validate_keepers(roll, keeper_values):
                return keeper_values
            else:
                print("Cheater!!! Or possibly made a typo...")
                print(self.format_roll(roll))

    # def zilch(self, rolled_dice):
    #     if len(GameLogic.get_scorers(rolled_dice)) == 0:
    #         self.validate_dice()
    #         return True

    #     return False

    
    # def validate_dice(self, rolled_dice, roller):
    #     print(f"{GameLogic.calculate_score(rolled_dice)} score")
    #     if GameLogic.calculate_score(rolled_dice) == 0:
    #         print("****************************************")
    #         print("**        Zilch!!! Round over         **")
    #         print("****************************************")
    #         self.banker.clear_shelf()
    #         self.bank_earned_points()
    #     else:
    #         print("Enter dice to keep or (q)uit:")
    #         response = input(">")
    #         if response:
    #             response = response.replace(" ", "")
    #         else:
    #             self.validate_dice(rolled_dice, roller)
    #     if response == "q":
    #         print(f"Thanks for playing. You earned {self.banker.balance} points")
    #         sys.exit()
    #     else: 
    #         # print("Cheater!!! Or possibly made a typo...")
    #         return self.validate_dice(rolled_dice, roller)


    def start_round(self, roller):

        new_round = True
        cheater_or_typo = False
        while self.status and self.banker.balance <= 10000:
            if new_round:
                self.rounds += 1
                print(f"Starting round {self.rounds}")
            if not cheater_or_typo:
                print(f"Rolling {self.dice_quantity} dice...")
            roll = roller(self.dice_quantity)
           
                
            roller_str = " "
            roller_str = " ".join(map(str, roll))
            # roller_str = " "
            # for num in roll:
            #     roller_str += str(num) + " "
            print(f"*** {roller_str} ***")
            if self.is_zilch(roll):
                self.do_zilch()
                self.dice_quantity = 6
                self.start_round(roller)
                
            
            
            print(f"Enter dice to keep, or (q)uit:")
            response = input("> ")
           
            
            if response == "q":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                sys.exit()
            else:
                cheater_or_typo = False
                user_response = tuple(map(int, list(response)))
                
                if not GameLogic.validate_keepers(roll, user_response):
                    new_round = False
                    cheater_or_typo = True
                    print("Cheater!!! Or possibly made a typo...")
                    continue

                self.dice_quantity -= len(user_response)
                score = GameLogic.calculate_score(user_response)
                self.banker.shelf(score)
                print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")
                print(f"(r)oll again, (b)ank your points or (q)uit:")
                response = input("> ")

            if response == "b":
                new_round = True
                self.dice_quantity = 6
                print(f"You banked {self.banker.shelved} points in round {self.rounds}")
                self.banker.bank()
                print(f"Total score is {self.banker.balance} points")
                continue
                
               

            elif response == "r":
                new_round = False
                if self.dice_quantity == 0:
                    self.dice_quantity = 6

            elif response == "q":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                sys.exit()


if __name__ == "__main__":
    game = Game()
    game.play()