import random
import pygame
from flags import *


# this class handle the movement of all the particles
class ArrPos:
    def __init__(self, array, width, height, display):
        self.array = array
        self.width = width
        self.height = height
        self.display = display

    def add(self, element):
        self.array.append(element)

    def update_positions(self):
        for i in self.array:
            # Updating position
            offset = random.random()
            i.new_vel()  # we need to randomize the force, so we are getting new values for the velocity
            i.x = i.x + i.Vx + offset
            i.y = i.y + i.Vy + offset

            # Checking if it's out of the screen
            if i.y > self.height:
                i.y = 0
            if i.y < 0:
                i.y = self.height
            if i.x >= self.width:
                i.x = 0
            if i.x < 0:
                i.x = self.width
            # Draw the rectangle
            for j in self.array:
                if i.check_collision(j):
                    i.color = BLACK
            pygame.draw.rect(self.display, i.color, (i.x, i.y, 10, 10))


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
        if (self.x < obj.x < self.x + 10 or self.x < obj.x + 10 < self.x + 10) and (self.y < obj.y < self.y + 10 or self.y < obj.y + 10 < self.y + 10):
            return True
        return False
