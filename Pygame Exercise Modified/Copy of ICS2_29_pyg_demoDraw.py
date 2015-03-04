import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###

pygame.init() 
window = pygame.display.set_mode((468, 480)) 
pygame.display.set_caption('Pygame Title Example 2') 
screen = pygame.display.get_surface() 
myfont = pygame.font.SysFont("Times New Roman", 25)
test=pygame.display.get_driver()

running = 1

point1= (0,0)
point2= (200,100)

print test  #gets printed on the output screen

# The screen is the Drawing window
screen.fill(THECOLORS['red'])

# Setting up the font and the size 
myfont = pygame.font.SysFont("Times New Roman", 25)
test=pygame.display.get_driver()

# Blit text to a certain x, y(18, 153) and of color r,g,b (0,0,0) which is black
text=myfont.render("Hello world", True, THECOLORS["black"])
screen.blit(text, (18,153))

#Where to draw, what color, from, to, (optional size)
pygame.draw.line(screen, THECOLORS['blue'], (0,0), (100,100))
pygame.draw.line(screen, THECOLORS['red'], (0,20), (100,20))

pygame.draw.circle(screen, THECOLORS['yellow'], (30,30), 30)

pygame.display.flip()



# Event Handling #
running=True
try:
    while running:

        events=pygame.event.get()

        for event in events: 
          if event.type == QUIT:
            print event
            running=False   # Stop the program, it's detected quit...
  
finally:
    pygame.quit()  # Keep this IDLE friendly 



        
        
