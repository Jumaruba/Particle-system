import pygame
from flags import *
import random
from rectpos import *
import sys
import neat


def config_pygame():
    global DISPLAY, square, clock
    pygame.init()
    square = RectPos(50, 50, 2, 2)
    clock = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((1024, 768))
    DISPLAY.fill(WHITE)
    return DISPLAY


def game(genomes, config):
    nets = []
    ge = []
    squares = []

    # for i in range(1, 200):
    for _, g in genomes:
        x_pos = random.uniform(0, 1024)
        y_pos = random.uniform(0, 768)

        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        obj = RectPos(x_pos, y_pos, 10, 10, BLUE)
        g.fitness = 0
        ge.append(g)
        pygame.draw.rect(DISPLAY, RED, (obj.x, obj.y, SIZE, SIZE))
        squares.append(obj)

    while True:
        for event in pygame.event.get():
            # Handle the key input
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Draw the game
        clock.tick(FPS)
        DISPLAY.fill(WHITE)
        # Draw the little squares

        for x, i in enumerate(squares):
            collision = False  # checks if for x happened a collision
            # Updating position
            offset = random.random()
            i.new_vel()  # we need to randomize the force, so we are getting new values for the velocity
            i.x = i.x + i.Vx + offset
            i.y = i.y + i.Vy + offset

            # Checking if it's out of the screen
            if i.y > HEIGHT:
                i.y = 0
            if i.y < 0:
                i.y = HEIGHT
            if i.x >= WIDTH:
                i.x = 0
            if i.x < 0:
                i.x = WIDTH
            # Draw the rectangle
            for j, s in enumerate(squares):
                if i.check_collision(s):
                    ge[x].fitness -= 1  # reduce the genome
                    squares.pop(x)  # remove the collided square
                    nets.pop(x)
                    ge.pop(x)

                    ge[j].fitness -= 1  # handling the other square
                    squares.pop(j)
                    nets.pop(j)
                    ge.pop(j)

                    collision = True
                    break

            if not collision:
                pygame.draw.rect(DISPLAY, RED, (i.x, i.y, SIZE, SIZE))
                ge[x].fitness += 2

        # Draw main rectangle

        pygame.display.update()
