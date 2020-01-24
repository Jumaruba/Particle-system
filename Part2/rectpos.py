import random
from flags import *


class RectPos:
    def __init__(self, x, y, Vx, Vy, color=RED):
        self.x = x
        self.y = y
        self.Vx = float(Vx)
        self.Vy = float(Vy)
        self.accel = 0
        self.color = color

    # Randomize the acceleration
    def randomize_accel(self):
        self.accel = random.normalvariate(MU, 0.2)
        return self.accel

    # New valor to the velocity
    def new_vel(self):
        self.randomize_accel()
        self.Vx += self.accel
        self.randomize_accel()
        self.Vy += self.accel

    def check_collision(self, obj):
        if self == obj:
            return False
        if (self.x < obj.x < self.x + SIZE or self.x < obj.x + SIZE < self.x + SIZE) and (
                self.y < obj.y < self.y + SIZE or self.y < obj.y + SIZE < self.y + SIZE):
            return True
        return False
