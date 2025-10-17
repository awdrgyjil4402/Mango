import pygame as py

class Player:
    def __init__(self):
        self.rect = py.Rect(100, 100, 25, 50)
        self.pos_x  = self.rect.x
        self.pos_y = self.rect.y
        self.vel_x = 0
        self.vel_y = 0
        self.acc = 200
        self.speed = 400
        self.jump_acc = -1500
        self.gravity = 5000
        self.on_ground = False

    def move(self, dt):
        keys = py.key.get_pressed()
        if keys[py.K_a]:
            if abs(self.vel_x) <= self.speed:
                self.vel_x -= self.acc
            self.pos_x -= self.vel_x * dt
        if keys[py.K_d]:
            if abs(self.vel_x) <= self.speed:
                self.vel_x += self.acc
            self.pos_x += self.vel_x * dt
        if keys[py.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_acc
            self.on_ground = False

        self.rect.x = round(self.pos_x)

    def physx(self, dt):
        # Gravity
        if self.vel_y <= 6000:
            self.vel_y += self.gravity * dt
        self.pos_y += self.vel_y * dt
        self.rect.y = round(self.pos_y)


    def collide(self, others):
        for rect in others:
            if self.rect.colliderect(rect):
                if self.vel_y > 0 and self.rect.bottom > rect.top:
                    self.rect.bottom = rect.top
                    self.pos_y = self.rect.y
                    self.vel_y = 0
                    self.on_ground = True
                if self.vel_y < 0 and self.rect.top < rect.bottom:
                    self.rect.top = rect.bottom
                    self.pos_y = self.rect.y
                    self.vel_y = 0


    def draw(self, screen):
        py.draw.rect(screen, (0, 0, 200), self.rect)
        print('rect:', self.rect.x, self.rect.y, 'pos:', self.pos_x, self.pos_y, 'vel:', self.vel_x, self.vel_y, 'on_ground:', self.on_ground)