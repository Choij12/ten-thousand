import random, collections
from collections import Counter
from random import randint, sample


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    # def roll_dice(num_dice):
        # return tuple(randint(1, 6) for _ in range(0, num_dice))
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)

    # @staticmethod
    # def get_scorers(input_):
    #     result = []
    #     for num in input_:
    #         if num == 1 or num == 5:
    #             result.append(num)
    #     return result

    @staticmethod
    def get_scorers(rolled_dice):
        dice_count = collections.Counter(rolled_dice)
        scoring_dice = []
        for value in dice_count:
            if value == 1 or value == 5:
                for x in range(dice_count[value]):
                    scoring_dice.append(value)
            else:
                if dice_count[value] > 2:
                    for x in range(dice_count[value]):
                        scoring_dice.append(value)
        return tuple(scoring_dice)

    # @staticmethod
    # def validate_keepers(roll, keepers):
    #     rolled_data = list(roll)
    #     valid = True
    #     for num in keepers:
    #         if num in rolled_data:
    #             rolled_data.remove(num)
    #         else:
    #             valid = False
    #             break
    #     return valid


    @staticmethod
    def validate_keepers(roll, keepers):
        counted_dice_list = collections.Counter(roll)
        counted_keep_list = collections.Counter(keepers)
        for num in counted_keep_list:
            if counted_keep_list[num] > counted_dice_list[num]:
                return False
        return True


    @staticmethod
    def calculate_score(dice):
        score = 0
        count = Counter(dice[:6])
        straight = sorted(dice)
      
        if count[5] == 1 or count[5] == 2:
            score += 50 * count[5]
        if count[1] == 1 or count[1] == 2:
            score += 100 * count[1]

        if straight == [1, 2, 3, 4, 5, 6]:
            score = 1500
            return score

        pair_of_two = 0
        if count[1] == 2:
            pair_of_two += 1
        if count[2] == 2:
            pair_of_two += 1
        if count[3] == 2:
            pair_of_two += 1
        if count[4] == 2:
            pair_of_two += 1
        if count[5] == 2:
            pair_of_two += 1
        if count[6] == 2:
            pair_of_two += 1
        
        if pair_of_two == 3:
            score = 1500
            return score

        for i in range(1, 7):
            if i == 1 and count[1] == 3:
                score += 1000
            elif i != 1 and count[i] == 3:
                score += i * 100
            
        for i in range(1, 7):
            if i == 1 and count[1] == 4:
                score += 2000
            elif i != 1 and count[i] == 4:
                score += i * 100 * 2

        for i in range(1, 7):
            if i == 1 and count[1] == 5:
                score += 3000
            elif i != 1 and count[i] == 5:
                score += i * 100 * 3

        for i in range(1, 7):
            if i == 1 and count[1] == 6:
                score += 4000
            elif i != 1 and count[i] == 6:
                score += i * 100 * 4

        return score





        # return tuple(randint(1,6) for _ in range(0,num_dice))
        # # or
        # # return tuple(sample(range(1, 6 + 1), num_dice))