# Import pygame and all the other modules you will be using import
import pygame, sys,os, time
from pygame.locals import *
from pygame.color import THECOLORS
from random import randint

## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###

# Set up pygame
pygame.init() 
clock=pygame.time.Clock()

# Set up the window and the size
window = pygame.display.set_mode((468, 480)) 
pygame.display.set_caption('Pygame Animation Example') 

# Set up the user screen 
screen = pygame.display.get_surface()

# Set up the font and the size 
myfont = pygame.font.SysFont("Times New Roman", 25)

# Fill the screen with a certain colour
screen.fill(THECOLORS["pink"])


# Main Game Loop #
running = True
try:
    while running:
       # Set up text message to display using the myfont settings (MSG in string, always True, what colour)
        text=myfont.render("Animating.", True, THECOLORS["black"])
        # Place (or blit) text on certain location (x, y) of the screen
        screen.blit(text,(0,0))
	pygame.draw.circle(screen, THECOLORS['yellow'], (30,30), 30)

        pygame.display.flip()
		
        pygame.time.delay(1000)

        screen.fill((255,255,255)) # can use THECOLORS["black"] instead of (255,255,255)
	pygame.draw.circle(screen, THECOLORS['yellow'], (35,30), 30)

        pygame.display.flip()


        # Set up text message to display using the myfont settings (MSG in string, always True, what colour)
        text=myfont.render("Animating..", True, THECOLORS["black"])
        # Place (or blit) text on certain location (x, y) of the screen
        screen.blit(text,(0,0))
        pygame.display.flip()
        pygame.time.delay(1000)

        screen.fill(THECOLORS["pink"])
        pygame.display.flip()

        # Set up text message to display using the myfont settings (MSG in string, always True, what colour)
        text=myfont.render("Goodbye", True, THECOLORS["black"])
        # Place (or blit) text on certain location (x, y) of the screen
        screen.blit(text,(0,0))
        # Update the users screen, this line must be run in order for the user to see changes
        pygame.display.flip()
        pygame.time.delay(1000)
        screen.fill(THECOLORS["pink"])

        pygame.display.flip() 

        # Checking event Loop #
        events=pygame.event.get()
        for event in events: 
          if event.type == QUIT:
             running=False   # Stop the program, it's detected quit...

        clock.tick(30) #setting the framerate (30 fps)
  
finally:
    pygame.quit()  # Keep this IDLE friendly 


        
