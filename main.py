import pygame
from pygame import mixer
import sys
from Player import player

pygame.init()
pygame.display.set_caption("BlockPusher")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

mixer.init()

Music = pygame.mixer.Sound("WadeInTheWater.mp3")

#classes and class arguments
player_pos = pygame.Vector2(400, 400)
player_size = pygame.Vector2(50, 50)

p1 = player(player_pos, player_size)



StartButton = pygame.Rect(325, 350, 200, 100)
HouseEntrance = pygame.Rect(362, 114, 52, 86)
HouseBorder = pygame.Rect(100, 0, 600, 200)
BedroomExit = pygame.Rect(770, 700, 100, 100)
Table = pygame.Rect(0, 40, 100, 150)
ExitShelf = pygame.Rect(730, 50, 50, 50)
DialougeBox = pygame.Rect(100, 600, 500, 150)
RiverBox = pygame.Rect(260, 0, 150, 20)
ForestExit = pygame.Rect(775, 265, 40, 100)
Train = pygame.Rect(150, 0, 520, 250)

BROWN = (234, 165, 108)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (115, 180, 255)
GREEN = (115, 255, 122)

#mouse_still = False

def main():

    House = pygame.image.load("EngUnessayHouse.png")
    Bedroom = pygame.image.load("KidBedroom.png")
    TableTop = pygame.image.load("TableTop.png")
    Narrative = pygame.image.load("Narrative.png")
    Forest1 = pygame.image.load("Forest1.png")
    Forest2 = pygame.image.load("Forest2.png")
    TrainStation = pygame.image.load("TrainStation.png")
    Ticket = pygame.image.load("Ticket.png")
    
    HasBeenPlayed = False

    #variables
    State = 1
    MouseDown = False
    searching = False
    TextCounter = 0

    running = True
    clock.tick(60)

    text_font = pygame.font.SysFont("Sans", 30, bold = True)

    def draw_text(text, font, text_col, tx, ty):
        img = font.render(text, True, text_col)
        screen.blit(img, (tx, ty))

    while running: #GAME LOOP####################################


        #event section------------------------------------
        for event in pygame.event.get():
            mouseX, mouseY = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                MouseDown = True
                if State == 4 and DialougeBox.collidepoint(mouseX, mouseY):
                    TextCounter += 1
                elif State == 5:
                    TextCounter += 1
                elif State == 9:
                    TextCounter += 1

        #print(TextCounter)



        keys = pygame.key.get_pressed()

        PlayerRect = pygame.Rect(p1.pos.x, p1.pos.y, 50, 50)

    

        #physics---------------------------------------------------
        #print(mouseX, mouseY)
        #Player movement
        if State != 4:
            p1.move(keys)
    
        #Is the MB1 being clicked?
        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            MouseDown = False

        #Render section----------------------------------------------
        #state 1
        if State == 1:
            screen.fill((0, 0, 0))

            #start button
            pygame.draw.rect(screen, (10, 200, 10), (325, 350, 200, 100))
            #start button collision
            if StartButton.collidepoint(mouseX, mouseY):
                pygame.draw.rect(screen, (10, 225, 10), (325, 350, 200, 100))
                if MouseDown:
                    State = 2
        
        #state 2
        if State == 2:
            screen.fill(BROWN)

            screen.blit(House, (0,0))
            print(p1.vx, p1.vy)
            if HouseBorder.colliderect(PlayerRect):
                if p1.pos.x + 50 > 100 and p1.pos.x + 50 < 105:
                    p1.pos.x = 50
                if p1.pos.x < 700 and p1.pos.x > 695:
                    p1.pos.x = 700
                if p1.pos.y < 200 and p1.pos.x+50 > 100 and p1.pos.x < 700:
                    p1.pos.y = 200
            if HouseEntrance.colliderect(PlayerRect):
                State = 3
            
            p1.draw(screen)
        
        #state 3
        if State == 3:
            screen.fill(BLUE)

            screen.blit(Bedroom, (0,0))

            if Table.collidepoint(mouseX, mouseY):
                pygame.draw.rect(screen, (255,255,255), (35, 130, 100, 50))

                if MouseDown:
                    searching = True

            if searching == True:
                screen.blit(TableTop, (0,0))
                if ExitShelf.collidepoint(mouseX, mouseY) and MouseDown:
                    searching = False

            if BedroomExit.colliderect(PlayerRect):
                p1.pos.x = 390
                p1.pos.y = 350
                State = 4

            if not searching:
                p1.draw(screen)

        if State == 4:
            screen.fill(BROWN)

            screen.blit(House, (0,0))

            #People
            pygame.draw.rect(screen, (WHITE), (430, 420, 50, 50))
            pygame.draw.rect(screen, (WHITE), (350, 420, 50, 50))

            #dialouge
            pygame.draw.rect(screen, (WHITE), (100, 600, 650, 150))
            pygame.draw.rect(screen, (BLACK), (95, 595, 655, 155), 5)

            if TextCounter == 1:
                draw_text("Owner:", text_font, (BLACK), 120, 630)
                draw_text("Did I just catch you comin' out of our home, negro?", text_font, (BLACK), 120, 670)
            elif TextCounter == 2:
                draw_text("Owner:", text_font, (BLACK), 120, 630)
                draw_text("What the f**k do you think y'er doin'?", text_font, (BLACK), 120, 670)
            elif TextCounter == 3:
                draw_text("Owner:", text_font, (BLACK), 120, 630)
                draw_text("That's it, I'm sendin' ya to the Slave Breaker.", text_font, (BLACK), 120, 670)
            elif TextCounter == 4:
                draw_text("Owner:", text_font, (BLACK), 120, 630)
                draw_text("Honey, go inside and write a letter to Edward Covey.", text_font, (BLACK), 120, 670)
            elif TextCounter == 5:
                draw_text("Owner:", text_font, (BLACK), 120, 630)
                draw_text("After a visit with him, you gon' learn to behave", text_font, (BLACK), 120, 670)
                draw_text("yourself, damn dirty negro.", text_font, (BLACK), 120, 700)
            elif TextCounter == 6:
                State = 5
            p1.draw(screen)

        if State == 5:
            screen.fill(WHITE)

            pygame.draw.line(screen, (BLACK), (0, 400), (800, 400), 20)

            screen.blit(Narrative, (0,0))

            draw_text("Narrator:", text_font, (BLACK), 20, 420)
            
            if TextCounter == 7:
                draw_text("A slave breaker is often defined as someone", text_font, (BLACK), 20, 460)
                draw_text("who was hired to \"discipline\" or brutalize enslaved people", text_font, (BLACK), 20, 500)
                draw_text("who were seen as rebellious, disobedient, or hard to control.", text_font, (BLACK), 20, 540)
            elif TextCounter == 8:
                draw_text("But, it doesn't end there...", text_font, (BLACK), 20, 460)
            elif TextCounter == 9:
                draw_text("A whip's lash would tear through the skin, sometimes leaving", text_font, (BLACK), 20, 460)
                draw_text("deep, jagged gashes. The force of the lash could even rip into ", text_font, (BLACK), 20, 500)
                draw_text("muscle tissue, exposing raw flesh underneath. The whip marks", text_font, (BLACK), 20, 540)
                draw_text("could be as deep as a few inches and would leave", text_font, (BLACK), 20, 580)
                draw_text("the victim exposed to infections, such as gangrene and sepsis,", text_font, (BLACK), 20, 620)
            elif TextCounter == 10:
                draw_text("which could lead to death if untreated.", text_font, (BLACK),20, 460)
            elif TextCounter == 11:
                draw_text("despite going through this, you resolve to escape using the", text_font, (BLACK),20, 460)
                draw_text("music that you heard your fellow slaves sing while at Covey's", text_font, (BLACK),20, 500)
            elif TextCounter == 12:
                State = 6
                p1.pos.x = 720
                p1.pos.y = 375
        
        if State == 6:
            screen.fill(GREEN)

            if HasBeenPlayed == False:
                HasBeenPlayed = True
                Music.play()
                Music.set_volume(0.5)


            if RiverBox.colliderect(PlayerRect):
                State = 7
                p1.pos.x = 400
                p1.pos.y = 720

            screen.blit(Forest1, (0,0))

            p1.draw(screen)

        if State == 7:
            screen.fill(GREEN)

            screen.blit(Forest2, (0,0))

            if ForestExit.colliderect(PlayerRect):
                p1.pos.x = 20
                p1.pos.y = 720
                State = 8

            p1.draw(screen)

        if State == 8:
            screen.fill((192,192,192))


            screen.blit(TrainStation, (0,0))

            if Train.colliderect(PlayerRect):
                State = 9

            p1.draw(screen)

        if State == 9:
            screen.fill(WHITE)

            screen.blit(Ticket, (0,0))


            pygame.draw.line(screen, (BLACK), (0, 400), (800, 400), 20)

            if TextCounter == 13:
                draw_text("Narrator:", text_font, (BLACK), 20, 420)
                draw_text("After your long and painful journey, you finally made it...", text_font,(BLACK), 20, 460)
            elif TextCounter == 14:
                draw_text("Conductor:", text_font, (BLACK), 20, 420)
                draw_text("ALL ABOARDDD!!! This is the A Line to New York.", text_font, (BLACK), 20, 460)
            elif TextCounter == 15:
                draw_text("Narrator:", text_font, (BLACK), 20, 420)
                draw_text("THE END", text_font,(BLACK), 20, 460)
            elif TextCounter == 16:
                running = False


            

        pygame.display.flip()

    #end of GAME LOOP##############################################
    pygame.quit()
    sys.exit()

if __name__ == "__main__":

    main()
