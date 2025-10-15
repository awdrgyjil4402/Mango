import pygame as py

class Player:
    def __init__(self):
        self.player_rect = py.Rect(100, 100, 50, 100)
        self.player_pos  = self.player_rect.x
        self.player_speed = 400

    def move(self, dt):
        keys = py.key.get_pressed()
        if keys[py.K_a]:
            self.player_pos -= self.player_speed * dt
        if keys[py.K_d]:
            self.player_pos += self.player_speed * dt

        self.player_rect.x = round(self.player_pos)

    def draw(self, screen):
        py.draw.rect(screen, (0, 0, 200), self.player_rect)