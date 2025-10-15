import pygame as py

class Player:
    def __init__(self):
        self.player_x = 100
        self.player_y = 100
        self.player_speed = 20

    def move(self):
        keys = py.key.get_pressed()
        if keys[py.K_a]:
            self.player_x -= self.player_speed
        if keys[py.K_d]:
            self.player_x += self.player_speed

    def draw(self, screen):
        py.draw.rect(screen, (0, 0, 200), (self.player_x, self.player_y, 50, 100))