import pygame
import pygame as py

class Level:
    def __init__(self):
        self.rect_1 = py.Rect(0, 600, 1080, 50)
        self.rect_2 = py.Rect(400, 400, 1080, 50)
        self.rect_3 = py.Rect(-600, 200, 1080, 50)
        self.level_rects = [self.rect_1, self.rect_2, self.rect_3]

    def draw(self, screen):
        for rect in self.level_rects:
            pygame.draw.rect(screen, (0, 200, 0), rect)