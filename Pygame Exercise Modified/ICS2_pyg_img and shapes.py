import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###



pygame.init() 
window = pygame.display.set_mode((1250, 800)) 
pygame.display.set_caption('Pygame Title Example 2') 
screen = pygame.display.get_surface()
myfont = pygame.font.SysFont("Vera", 25)
userin =""


file_name = "GC.jpg" # what's the filename of the picture along with extension
img_surface = pygame.image.load(file_name) #load it into memory
screen.blit(img_surface, (0,0)) # Blit img to a certain x,y

# Blit text to a certain x, y(18, 153) and of color r,g,b (0,0,0) which is black

# Blit a rectangle
# pygame.draw.rect(Surface, color, Rect, width=0)
pygame.draw.rect(screen, (255, 255, 255), (81, 353, 251, 50)  )
screen.blit(myfont.render("button1", 1, (0,0,0)), (117,363))

pygame.display.update() 
 
running = True
        
try:

    while running:

		# Anything you might want to repeat here...

	
        # Event Handling:
        events = pygame.event.get( )
        
        for e in events:
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
			
            print x, y, butt

            
            if( e.type == QUIT or (e.type==KEYDOWN and e.key==K_ESCAPE) ):
                screen.fill(THECOLORS["white"])
                screen.blit(myfont.render("Goodbye", 1, (0,0,0)), (0,0))
                pygame.display.update()            
                time.sleep(1)
                running = False
                
            elif (e.type == KEYDOWN):
             

                screen.fill(THECOLORS["white"])
                # Keyboard Input capture
                temp=pygame.key.name(e.key)
                if temp=="space":
                    print "pewpew"
                # You should check that the character is a text string before printing it
                
                userin=userin+temp
                screen.blit(myfont.render(userin, 1, (0,0,0)), (0,0))

                if( e.key == K_f ):
                    pygame.display.toggle_fullscreen()

        # Drawing finished this iteration?  Update the screen
        pygame.display.update()            


finally:
    pygame.quit()  # Keep this IDLE friendly 



