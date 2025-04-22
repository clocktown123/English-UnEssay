import pygame

class player:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.w = 50
        self.h = 50
    
    def move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.x -= 5
        if keys_pressed[pygame.K_RIGHT]:
            self.x += 5
        if keys_pressed[pygame.K_UP]:
            self.y -= 5
        if keys_pressed[pygame.K_DOWN]:
            self.y += 5

    def draw(self, screen):
        pygame.draw.rect(screen, (20, 20, 200), (self.x, self.y, self.w, self.h))
