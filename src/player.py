import pygame as py

class Player:
    def __init__(self):
        self.rect = py.Rect(100, 100, 25, 50)
        self.pos_x  = self.rect.x
        self.pos_y = self.rect.y
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 500
        self.jump_acc = -1500
        self.gravity = 5000
        self.on_ground = False

    def move(self, dt):
        keys = py.key.get_pressed()
        if keys[py.K_a]:
            self.pos_x -= self.speed * dt
        if keys[py.K_d]:
            self.pos_x += self.speed * dt
        if keys[py.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_acc
            self.on_ground = False

        self.rect.x = round(self.pos_x)

    def physx(self, dt):
        # Gravity
        if self.vel_y <= 7000:
            self.vel_y += self.gravity * dt
        self.pos_y += self.vel_y * dt
        self.rect.y = round(self.pos_y)

    def collide(self, other):
        if self.rect.colliderect(other):
            if self.vel_y > 0 and self.rect.bottom > other.top:
                self.rect.bottom = other.top
                self.pos_y = self.rect.y
                self.vel_y = 0
                self.on_ground = True
            if self.vel_y < 0 and self.rect.top < other.bottom:
                self.rect.top = other.bottom
                self.pos_y = self.rect.y
                self.vel_y = 0

    def draw(self, screen):
        py.draw.rect(screen, (0, 0, 200), self.rect)