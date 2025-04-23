import pygame

class player:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.w = 50
        self.h = 50
        self.vx = 0
        self.vy = 0
    
    def move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.vx = -.2
        elif keys_pressed[pygame.K_RIGHT]:
            self.vx = .2
        else:
            self.vx = 0
        if keys_pressed[pygame.K_UP]:
            self.vy = -.2
        elif keys_pressed[pygame.K_DOWN]:
            self.vy = .2
        else:
            self.vy = 0

        self.x+=self.vx
        self.y+=self.vy

    def draw(self, screen):
        pygame.draw.rect(screen, (20, 20, 200), (self.x, self.y, self.w, self.h))
