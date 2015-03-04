import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###


## Initial Setup stuff ##
pygame.init() 
window = pygame.display.set_mode((468, 480)) 
pygame.display.set_caption('Pygame Title Example 2') 
screen = pygame.display.get_surface()
myfont = pygame.font.SysFont("none", 23)



pygame.display.update() 
 
show='welcome'

# Main Program Loop starts here
running = True        
try:

    while running: #What do you want to do while the program is running
        
        # Depending on which show is used, show a different screen and buttons
        if show=="welcome":   #this is the screen you want to show at the beginning
            ## What else do you wan to show on this screen ? put it here ##
            screen.fill(THECOLORS["black"])
            screen.blit(myfont.render("WELCOME SCreEEn", 1, THECOLORS['red']), (0,0))

            # Blit a rectangle to be used as a button
            # pygame.draw.rect(Surface, color, (x,y,length, height), width=0)
            pygame.draw.rect(screen, THECOLORS['white'], (81, 353, 100, 50)  )

            # Blit text at certain location to  be caption of the button
            screen.blit(myfont.render("Start", 1, THECOLORS['black']), (90,363))

        

            
        # Event Handling
        events = pygame.event.get( ) #This command will read everything that is user doing something (an event)
        
        for e in events:
            pos = pygame.mouse.get_pos() # This will get the mouse's position and store it as (x,y) 
            butt = pygame.mouse.get_pressed() # This will get the mouse's buttons as (Left,Middle,Right)  0 if unpressed, 1 if pressed

            print pos, butt #prints debug info to the DOS screen


            
            
            if e.type == QUIT :
                
                screen.fill(THECOLORS["white"])
                screen.blit(myfont.render("Goodbye", 1, (0,0,0)), (0,0))
                pygame.display.update()            
                time.sleep(1)
                running = False
            if e.type == KEYDOWN :   # Only activate below if event was a keypress
                print "a key was pressed"
                # returns the key pressed as a string pygame.key.name(e.key)
                print "This was pressed: ", pygame.key.name(e.key)

                
                
                
    
            

        # Drawing finished this iteration?  Update the screen
        pygame.display.update()            


finally:
    pygame.quit()  # Keep this IDLE friendly 



