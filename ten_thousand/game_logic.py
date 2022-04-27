import random 
from collections import Counter
from random import randint, sample

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1, 6) for _ in range(0, num_dice))


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

        if count[2] == 2 and count[3] == 2 and count[6] == 2:
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