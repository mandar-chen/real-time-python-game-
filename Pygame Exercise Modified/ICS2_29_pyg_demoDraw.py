import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###

pygame.init() 
window = pygame.display.set_mode((640, 480)) 
pygame.display.set_caption('Exercise1') 
screen = pygame.display.get_surface() 

running = 1

point1= 0,0
point2= 200,100

# The screen is the Drawing window
screen.fill(THECOLORS['red'])

# Setting up the font and the size 
myfont = pygame.font.SysFont("Arial", 25)
test=pygame.display.get_driver()

# Blit text to a certain x, y(18, 153) and of color r,g,b (0,0,0) which is black
text=myfont.render("Hello World", True, THECOLORS["white"])
screen.blit(text, (50,100))

text2=myfont.render("Mandar Chen", True, THECOLORS["blue"])
screen.blit(text2, (50,130))

pygame.display.flip() # flip all changes onto the display window

#Where to draw, what color, from, to, (optional size)

pygame.draw.line(screen, THECOLORS['black'], (200,200), (250,200))

pygame.draw.line(screen, THECOLORS['white'], (225,170), (225,250))

pygame.draw.circle(screen, THECOLORS['yellow'], (225,170), 20)

pygame.draw.line(screen, THECOLORS['blue'], (225,250), (200,300))

pygame.draw.line(screen, THECOLORS['green'], (225,250), (250,300))

pygame.display.flip() # flip all changes onto the display window

pygame.draw.circle(screen, THECOLORS['white'], (400,400), 40)

pygame.draw.circle(screen, THECOLORS['red'], (400,400), 30)

pygame.draw.circle(screen, THECOLORS['white'], (400,400), 20)

pygame.draw.circle(screen, THECOLORS['red'], (400,400), 10)


time.sleep(1)
pygame.display.flip() # flip all changes onto the display window

# Event Handling: include it for now so that you can quit the program cleanly ###
running=True
try:
    while running:

        events=pygame.event.get()
        
        for event in events:
            print event.type
            if event.type == QUIT:
                print event
                running=False   # Stop the program, it's detected quit...
            
        
  
finally:
    pygame.quit()  # Keep this IDLE friendly     
        
# Event Handling End ##############################################################