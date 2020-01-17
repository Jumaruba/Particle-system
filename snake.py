import pygame, sys
from pygame.locals import *
from rect_pos import *
from Flags import *

pygame.init()
square = rect_pos(50, 50, 2, 2)
clock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((1024, 768))
DISPLAY.fill(WHITE)


# create 2 rectangles
manager = Arr_pos([], 1024, 768, DISPLAY)
for i in range(1, 100):
    x_pos = random.uniform(0, 1024)
    y_pos = random.uniform(0, 768)
    if i == 2:
        obj = rect_pos(x_pos, y_pos, 5, 5, BLUE)
    else:
        obj = rect_pos(x_pos, y_pos, INIT_ACCEL, INIT_ACCEL)
    pygame.draw.rect(DISPLAY, RED, (obj.x, obj.y, 10, 10))
    manager.add(obj)

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
    manager.update_positions()
    # Draw main rectangle

    pygame.display.update()
