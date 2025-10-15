import pygame as py
import player

# Initialize Pygame
py.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = py.display.set_mode(SIZE)
clock = py.time.Clock()
player = player.Player()

# Initialize global variables

running = True
while running:
    # EVENT HANDLING
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False    

    # GAME LOGIC
    player.move()

    # RENDERING
    screen.fill((255, 255, 255))  # always the first drawing command

    player.draw(screen)

    # Finish the game loop DO NOT TOUCH
    py.display.flip()
    clock.tick(30)

py.quit()