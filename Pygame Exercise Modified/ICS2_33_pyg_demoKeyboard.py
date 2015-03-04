import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###
whatkey=""

## Initial Setup stuff ##
pygame.init() 
window = pygame.display.set_mode((468, 480)) 
pygame.display.set_caption('Pygame Title Example 2') 
screen = pygame.display.get_surface()
myfont = pygame.font.SysFont("none", 23)



pygame.display.update() 
 

# Main Program Loop starts here
running = True        
try:

    while running: #What do you want to do while the program is running
        print whatkey            
        # Event Handling
        events = pygame.event.get( ) #This command will read everything that is user doing something (an event)
        
        for e in events:

            

            
            
            if e.type == QUIT :
                
                screen.fill(THECOLORS["white"])
                screen.blit(myfont.render("Goodbye", 1, (0,0,0)), (0,0))
                pygame.display.update()            
                time.sleep(1)
                running = False

            ## KEYBOARD INPUT COMMANDS ##    
            if e.type == KEYDOWN :  # check to see if a keyboard button was detected
                # Print to debug screen.
                print "key was pressed"
                # Command pygame.key.name(e.key) returns the key pressed as a string
                whatkey=pygame.key.name(e.key)
                print "The following key was pressed by the user: ", whatkey
                screen.blit(myfont.render(whatkey, 1, THECOLORS["white"]), (0,0))
                pygame.display.update()   # update the screen
                time.sleep(1)
                screen.fill(THECOLORS["black"])   #clear the screen after showing
                pygame.display.update()
    

                if whatkey=="escape":   #user pressed escape so we will quit
                    running = False
                    print "Goodbye"
                    time.sleep(1)
                
            if e.type == KEYUP:
                whatkey=""
            
        # Drawing finished this iteration?  Update the screen
        pygame.display.update()            


finally:
    pygame.quit()  # Keep this IDLE friendly 



