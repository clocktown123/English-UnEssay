import pygame

class player:
    def __init__(self, position, Size):
        self.pos = pygame.Vector2(position)
        self.size = pygame.Vector2(Size)
        self.vx = 0
        self.vy = 0
    
    def move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.vx = -1
        elif keys_pressed[pygame.K_RIGHT]:
            self.vx = 1
        else:
            self.vx = 0
        if keys_pressed[pygame.K_UP]:
            self.vy = -1
        elif keys_pressed[pygame.K_DOWN]:
            self.vy = 1
        else:
            self.vy = 0

        self.pos.x+=self.vx
        self.pos.y+=self.vy

    def draw(self, screen):
        pygame.draw.rect(screen, (20, 20, 200), (self.pos, self.size))
