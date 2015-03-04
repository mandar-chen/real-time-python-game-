#ICS Summative
#C. Mandar
#Completion date: January 31, 2012
#ICS Summative 

#Setting up the imports
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import random

#Dealing with the video driver issue
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Initialize
pygame.init() 
window = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption('Pygame Title Example 2') 
screen = pygame.display.get_surface()
myfont = pygame.font.SysFont("Vera", 25)

#User initialize
running = True
purchase1='no'
purchase2='no'
purchase3='no'
show='home' 

#Iniatilizing time
speed=0
week=1
month=0
year=0

#Initializing assets
userasset=1000
propertyasset1=300
propertyasset2=500
propertyasset3=700

#Initializing lists
pricerange1=[0,0,0,0,1]

#Initializing goal
goallevel="1"

#Initializing rent price
rentprice1=100
rentprice2=200
rentprice3=300

pygame.display.update() 
 
#Game component 

try:	
    while running:
        
        #The home display screen
        if show=='home':
            
            screen.fill(THECOLORS["white"])  
            screen.blit(myfont.render("The Investment Game", 1, THECOLORS['black']), (50,50))
            pygame.draw.rect(screen, THECOLORS['black'],(50, 100, 100, 50))
            screen.blit(myfont.render("Next", 1, THECOLORS['white']), (65,115))
        
        #The instructions display screen
        if show=='instructions':
            
            screen.fill(THECOLORS["white"])  
            
            #Main instructions component
            screen.blit(myfont.render("Instructions", 1, THECOLORS['black']), (50,50))
            screen.blit(myfont.render("1. Time and asset are displayed at top of the screen.", 1, THECOLORS['black']), (50,150))
            screen.blit(myfont.render("2. The price of unit is shown right below its icon.", 1, THECOLORS['black']), (50,200))
            screen.blit(myfont.render("3. If price goes up, a green rect will be shown.", 1, THECOLORS['black']), (50,250))
            screen.blit(myfont.render("4. If price goes down, a red rect will be shown.", 1, THECOLORS['black']), (50,300))
            screen.blit(myfont.render("5. If you own the unit, a green rect will shown on top.", 1, THECOLORS['black']), (50,350))
            screen.blit(myfont.render("6. Rent will be paid monthly if you own the unit.", 1, THECOLORS['black']), (50,400))
            
            pygame.draw.rect(screen, THECOLORS['black'],(50, 425, 100, 50))
            screen.blit(myfont.render("Start", 1, THECOLORS['white']), (65,430))
        
        #The game screen
        if show=="game":
            
            #Setting up the screen and the title of the page
            screen.fill(THECOLORS["white"])            
            
            #Setting up the housings
            
            #Unit 1 
            pygame.draw.rect(screen, THECOLORS['black'], (50, 100, 100, 50)  )
            screen.blit(myfont.render("Unit 1", 1, THECOLORS['white']), (65,115))
            propertyasset1=propertyasset1+pricerange1[random.randint(0,4)]
            screen.blit(myfont.render('$'+str(propertyasset1), 1, THECOLORS['black']), (65,155))
            
            #Unit 2
            pygame.draw.rect(screen, THECOLORS['black'], (50, 220, 100, 50)  )
            screen.blit(myfont.render("Unit 2", 1, THECOLORS['white']), (65,235))
            propertyasset2=propertyasset2+pricerange1[random.randint(0,4)]
            screen.blit(myfont.render('$'+str(propertyasset2), 1, THECOLORS['black']), (65,275))
            
            #Unit 3
            pygame.draw.rect(screen, THECOLORS['black'], (50, 340, 100, 50)  )
            screen.blit(myfont.render("Unit 3", 1, THECOLORS['white']), (65,355))
            propertyasset3=propertyasset3+pricerange1[random.randint(0,4)]
            screen.blit(myfont.render('$'+str(propertyasset3), 1, THECOLORS['black']), (65,395))
       
            #Managing the time
            screen.blit(myfont.render('W'+str(week),1, THECOLORS['black']), (0,0))
            screen.blit(myfont.render('M'+str(month),1, THECOLORS['black']), (30,0))
            screen.blit(myfont.render('Y'+str(year),1, THECOLORS['black']), (60,0))
            
            #Calculating the time
            speed=speed+1
            
            if speed==100:
                speed=0
                week=week+1
            
            if week==5:
                week=0
                month=month+1
                if purchase1=='yes':
                    userasset=userasset+rentprice1
                if purchase2=='yes':
                    userasset=userasset+rentprice2
                if purchase3=='yes':
                    userasset=userasset+rentprice3
                    
            if month==12:
                month=0
                year=year+1
                
            #Setting up the price of housing 
            if month==0 or month==1 or month==3 or month==5:
                pricerange1=[0,0,0,0,1]
                pygame.draw.rect(screen, THECOLORS['green'], (55, 157, 5, 12))
                pygame.draw.rect(screen, THECOLORS['green'], (55, 277, 5, 12))
                pygame.draw.rect(screen, THECOLORS['green'], (55, 397, 5, 12))
                
            if month==2 or month==4:
                pricerange1=[0,0,0,0,-1]
                pygame.draw.rect(screen, THECOLORS['red'], (55, 157, 5, 12))
                pygame.draw.rect(screen, THECOLORS['red'], (55, 277, 5, 12))
                pygame.draw.rect(screen, THECOLORS['red'], (55, 397, 5, 12))  
            
            if month==6 or month==7 or month==8:
                pricerange1=[0,0,0,1,1]
                pygame.draw.rect(screen, THECOLORS['green'], (55, 157, 5, 12))
                pygame.draw.rect(screen, THECOLORS['green'], (55, 277, 5, 12))
                pygame.draw.rect(screen, THECOLORS['green'], (55, 397, 5, 12))
                #Summer sales
                
            if month==9 or month==10:
                pricerange1=[0,0,0,-1,1]
                pygame.draw.rect(screen, THECOLORS['red'], (55, 157, 5, 12))
                pygame.draw.rect(screen, THECOLORS['red'], (55, 277, 5, 12))
                pygame.draw.rect(screen, THECOLORS['red'], (55, 397, 5, 12))  
            
            if month==11 or month==12:
                pricerange1=[0,0,1,1,1]
                pygame.draw.rect(screen, THECOLORS['green'], (55, 157, 5, 12))
                pygame.draw.rect(screen, THECOLORS['green'], (55, 277, 5, 12))
                pygame.draw.rect(screen, THECOLORS['green'], (55, 397, 5, 12))
                #Winter sales
            

            #Managing the money
            screen.blit(myfont.render('$'+str(userasset), 1, THECOLORS['black']), (0,20))
            
            #Indicating ownership
            if purchase1=='yes':
                pygame.draw.rect(screen, THECOLORS['green'], (50, 90, 10, 10))
            if purchase2=='yes':
                pygame.draw.rect(screen, THECOLORS['green'], (50, 210, 10, 10))
            if purchase3=='yes':
                pygame.draw.rect(screen, THECOLORS['green'], (50, 330, 10, 10))            
   
            #Managing the goal
            
            if goallevel=="1":  
                
                if userasset==1000 or 2000>userasset>1000:
                    screen.blit(myfont.render("Earn $2000", 1, THECOLORS['black']), (0,450))
                
                if 3000>userasset>2000:
                    screen.blit(myfont.render("Earn $1000 more", 1, THECOLORS['black']), (0,450))
                    pygame.draw.rect(screen, THECOLORS['black'], (0, 475, 250, 10))

                if userasset>3000:
                    screen.blit(myfont.render("Good job, here is a cheque of $5,000!", 1, THECOLORS['black']), (0,450))
                    pygame.draw.rect(screen, THECOLORS['black'], (0, 475, 500, 10))
                    userasset=userasset+5000
                    goallevel="2"
                                
        #Managing Events
        events = pygame.event.get( )
        
        for e in events:
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
            print x, y, butt 
            
            #Home screen
            if x>50 and x<50+100 and y>100 and y<100+50 and butt[0]==1 and show=="home":
                show="instructions" 
                
            #Instruction screen
            if x>50 and x<50+100 and y>425 and y<425+50 and butt[0]==1 and show=="instructions":
                show="game" 

            #Unit 1 purchase
            if x>50 and x<50+100 and y>100 and y<100+50 and butt[0]==1 and purchase1=='no' and show=="game":
                if userasset-propertyasset1>-1:
                    userasset=userasset-propertyasset1
                    purchase1='yes'
                else:
                    screen.blit(myfont.render("You do not have enough asset.", 1, THECOLORS['red']), (100,0))
                     
                
            elif x>50 and x<50+100 and y>100 and y<100+50 and butt[2]==1 and purchase1=='yes'and show=="game":
                userasset=userasset+propertyasset1
                purchase1='no'
            
            #Unit 2 purchase
            if x>50 and x<50+100 and y>220 and y<220+50 and butt[0]==1 and purchase2=='no'and show=="game":
                if userasset-propertyasset2>-1:
                    userasset=userasset-propertyasset2
                    purchase2='yes'
                else:
                    screen.blit(myfont.render("You do not have enough asset.", 1, THECOLORS['red']), (100,0))
                
            elif x>50 and x<50+100 and y>220 and y<220+50 and butt[2]==1 and purchase2=='yes'and show=="game":
                userasset=userasset+propertyasset2
                purchase2='no'
                
            #Unit 3 purchase
            if x>50 and x<50+100 and y>340 and y<340+50 and butt[0]==1 and purchase3=='no'and show=="game":
                if userasset-propertyasset3>-1:
                    userasset=userasset-propertyasset3
                    purchase3='yes'
                else:
                    screen.blit(myfont.render("You do not have enough asset.", 1, THECOLORS['red']), (100,0))
            
            elif x>50 and x<50+100 and y>340 and y<340+50 and butt[2]==1 and purchase3=='yes'and show=="game":
                userasset=userasset+propertyasset3
                purchase3='no'
                
            #Quitting the game
            if( e.type == QUIT or (e.type==KEYDOWN and e.key==K_ESCAPE) ):
                screen.fill(THECOLORS["white"])
                screen.blit(myfont.render("Goodbye", 1, (0,0,0)), (0,0))
                pygame.display.update()            
                time.sleep(1)
                running = False
                
        pygame.display.update()            


finally:
    pygame.quit()  # Keep this IDLE friendly 



