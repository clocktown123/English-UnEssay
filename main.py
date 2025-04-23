import pygame
import sys
from Player import player

p1 = player()



pygame.init()
pygame.display.set_caption("BlockPusher")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

def main():
    running = True
    clock.tick(60)
    while running: #GAME LOOP####################################
        #event section------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            
        keys = pygame.key.get_pressed()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     Mshoot = True
        
        #physics---------------------------------------------------

        p1.move(keys)

        #Render section
        
        screen.fill((0, 0, 0))

        p1.draw(screen)

        pygame.display.flip()

    #end of GAME LOOP##############################################
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
