# Part of "Scientific Computing with Python Certification" on FreeCodeCamp
# Calculates an approximate probability simulating a given number of experiments without replacement

import copy
import random
from collections import Counter

class Hat:
    def __init__(self,**balls):
        self.contents = []
        for k,v in balls.items(): self.contents = self.contents + [k]*v

    def draw(self,num_todraw):
        if num_todraw > len(self.contents): num_todraw = len(self.contents)
        self.drawn_balls = []
        for n in range(num_todraw):
            self.ball = random.choice(self.contents)
            self.drawn_balls.append(self.ball)
            self.contents.remove(self.ball)
        self.drawn_balls_counter = Counter(self.drawn_balls)
        return self.drawn_balls

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    M = 0
    initial = copy.deepcopy(hat.contents)
    for n in range(num_experiments):
        hat.contents.clear()
        for i in initial: hat.contents.append(i)
        hat.draw(num_balls_drawn)
        if all(hat.drawn_balls_counter[k]>=v for k,v in expected_balls.items()):
            M +=1
    probability = M/num_experiments
    return probability
