from p5 import *
from random import randint
import keyboard as kb

class Snake:
    def __init__(self, size):
        self.size = size
        self.initialize()
    
    def update(self):
        self.pos += self.speed * self.size
        self.tail[0] = self.pos
        if len(self.tail) > 1:
            self.tail.insert(0, self.tail[len(self.tail) - 1])
            self.tail.pop()
        
        if self.death():
            print(f'You Dead.  Score:  {len(self.tail)}!')
            self.reset()
        
    def reset(self):
        self.initialize()

    def initialize(self):
        self.pos = Vector(randint(0, width // self.size) * size, randint(0, height // self.size) * self.size)
        self.tail = [self.pos]
        self.speed = Vector(0,0)
    
    def death(self):
        if self.pos.x < 0 or self.pos.x > width - self.size or self.pos.y < 0 or self.pos.y > height - self.size:
            return True
        for i in range(2, len(self.tail)):
            if self.pos == self.tail[i]:
                return True

    def add(self):
        self.tail.append(self.pos + self.speed * self.size)
    
    def show(self):
        fill(0)
        for i in range(0, len(self.tail)):
            rect(self.tail[i], self.size, self.size)
            print(f'Score: {len(self.tail)}', end = '\r')

    def control(self):
        if kb.is_pressed('UP'):
            self.speed = Vector(0, -1)
        if kb.is_pressed('DOWN'):
            self.speed = Vector(0, 1)
        if kb.is_pressed('LEFT'):
            self.speed = Vector(-1, 0)
        if kb.is_pressed('RIGHT'):
            self.speed = Vector(1, 0)
def setup():
    size(500, 500)
    title = "Snake Game"

