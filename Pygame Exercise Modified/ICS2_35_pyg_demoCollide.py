import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###
clock=pygame.time.Clock()


## Initial Setup stuff ##
pygame.init() 
window = pygame.display.set_mode((468, 480)) 
pygame.display.set_caption('Pygame Title Example 2') 
screen = pygame.display.get_surface()
myfont = pygame.font.SysFont("none", 23)



pygame.display.update() 
 
show='welcome'
x=0
y=0
xdir=1
ydir=5
mx=0
my=0



# Main Program Loop starts here
running = True        
try:

    while running: #What do you want to do while the program is running

        
        x=x+xdir
        y=y+ydir
        screen.fill((255,255,255)) # can use THECOLORS["black"] instead of (255,255,255)
        pygame.draw.circle(screen, THECOLORS['red'], (mx,my), 30)
        
        d=((y-my)**2+(x-mx)**2)**(0.5)
        print d
        
        if d<60:
            print "I HIT YOU"
        
        
        pygame.draw.circle(screen, THECOLORS['yellow'], (x,y), 30)

        
        if x >= 468:
            xdir=-xdir
        elif x<0:
            xdir=-xdir
        elif y<0:
            ydir=-ydir
        elif y>468:
            ydir=-ydir
        #print x,y
            
        # Event Handling
        events = pygame.event.get( ) #This command will read everything that is user doing something (an event)
        
        for e in events:
            pos = pygame.mouse.get_pos() # This will get the mouse's position and store it as (x,y)
            mx=pos[0]
            my=pos[1]
            
            butt = pygame.mouse.get_pressed() # This will get the mouse's buttons as (Left,Middle,Right)  0 if unpressed, 1 if pressed

            #print pos, butt #prints debug info to the DOS screen



            
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
        clock.tick(30)

finally:
    pygame.quit()  # Keep this IDLE friendly 



