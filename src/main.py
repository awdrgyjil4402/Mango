import pygame as py, time
import player

# Initialize Pygame, other libraries, variables
py.init()

WIDTH = 1080
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)

screen = py.display.set_mode(SIZE)
clock = py.time.Clock()
player = player.Player()

previous_frame_time = time.time()

running = True
while running:
    # Get the delta time
    dt = time.time() - previous_frame_time
    previous_frame_time = time.time()

    # EVENT HANDLING
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False    

    # GAME LOGIC
    player.move(dt)
    player.physx(dt)

    # RENDERING
    screen.fill((255, 255, 255))  # always the first drawing command
    player.draw(screen)

    # Finish the game loop DO NOT TOUCH
    py.display.flip()

py.quit()