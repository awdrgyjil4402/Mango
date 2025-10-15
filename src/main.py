import pygame as py

# Initialize Pygame
py.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = py.display.set_mode(SIZE)
clock = py.time.Clock()

# Initialize global variables
player_x = 100
player_y = 100
player_speed = 20

running = True
while running:
    # EVENT HANDLING
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False    

    # GAME LOGIC
    keys = py.key.get_pressed()
    if keys[py.K_a]:
        player_x -= player_speed
    if keys[py.K_d]:
        player_x += player_speed

    # RENDERING
    screen.fill((255, 255, 255))  # always the first drawing command

    py.draw.rect(screen, (0,0,200), (player_x, player_y, 50, 100))

    # Finish the game loop DO NOT TOUCH
    py.display.flip()
    clock.tick(30)

py.quit()