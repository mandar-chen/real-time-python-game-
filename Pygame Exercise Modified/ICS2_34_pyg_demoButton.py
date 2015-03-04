import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
playerasset=500000

## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###


## Initial Setup stuff ##
pygame.init() 
window = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption('Pygame Title Example 2') 
screen = pygame.display.get_surface()
myfont = pygame.font.SysFont("Vera", 25)
userin =""

pygame.display.update() 
 
running = True
show='welcome'
        
try:
    while running:        
        # Depending on which show is used, show a different screen and buttons
        if show=="welcome":   #this is the screen you want to show at the beginning
            ## What else do you want to show on this screen ? put it here ##
            screen.fill(THECOLORS["black"])
            screen.blit(myfont.render("Welcome to Real Estate Sim!", 1, THECOLORS['white']), (125,75))

            # Blit a rectangle to be used as a button
            # pygame.draw.rect(Surface, color, (x,y,length, height), width=0)
            pygame.draw.rect(screen, THECOLORS['white'], (50, 300, 125, 50))

            # Blit text at certain location to  be caption of the button
            screen.blit(myfont.render("Start", 1, THECOLORS['black']), (85,325))
        elif show=='start':   # this is the screen to be used for start screen
            ## What else do you wan to show on this screen ? put it here ##
            screen.fill(THECOLORS["black"])
            screen.blit(myfont.render("How to Play?", 1, THECOLORS['white']), (125,75))
            
            # Blit a rectangle to be used as a button
            # pygame.draw.rect(Surface, color, (x,y,length, height), width=0)
            pygame.draw.rect(screen, THECOLORS['white'], (50, 300, 125, 50)  )

            # Blit text at certain location to  be caption of the button
            screen.blit(myfont.render("Next", 1, THECOLORS['black']), (85,325))
            screen.blit(myfont.render(str(playerasset), 1, THECOLORS['white']), (0,20))


            
        # Event Handling:
        events = pygame.event.get( )
        
        for e in events:
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
            print x, y, butt #prints debug info to the DOS screen
            

            # Detecting the click inside the button area
            if x>50 and x<50+125 and y>300 and y<300+50 and butt[0]==1 and show=='welcome':
                playerasset=playerasset+10000
                screen.blit(myfont.render(str(playerasset), 1, THECOLORS['white']), (0,20))
                show='start'  #User was on 'welcome' and button clicked, so change screen to 'start'
            elif x>81 and x<81+100 and y>353 and y<353+50 and butt[0]==1 and show=='start':
                show='welcome' #User was on 'start' and button clicked, so change screen to 'welcome'
            

            if e.type==KEYDOWN:
                if e.key==K_SPACE:
                    print "sadsadsadsadsadsadsadsa"
                    
            
            if( e.type == QUIT or (e.type==KEYDOWN and e.key==K_ESCAPE) ):
                screen.fill(THECOLORS["white"])
                screen.blit(myfont.render("Goodbye", 1, (0,0,0)), (0,0))
                pygame.display.update()            
                time.sleep(1)
                running = False
                


        # Drawing finished this iteration?  Update the screen
        pygame.display.update()            


finally:
    pygame.quit()  # Keep this IDLE friendly 



