"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Dodge Ball")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x=350
y=250
x_offset=5
y_offset=5
#left one
x_speed = 0
y_speed = 0
y_coord = 10
#right one


 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_a:
                x_speed = -5
            elif event.key == pygame.K_d:
                x_speed = 5
            elif event.key == pygame.K_w:
                y_speed = -5
            elif event.key == pygame.K_s:
                y_speed = 5

        elif event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0
            elif event.key == pygame.K_s or event.key == pygame.K_w:
                y_speed = 0
        
    y_coord+=y_speed
    # --- Game logic should go here
    x=x+x_offset
    if x==0 or x==675:
        x_offset=x_offset*(-1)
        x=x+x_offset

    y=y+y_offset
    if y==0 or y==490:
        y_offset=y_offset*(-1)
        y=y+y_offset

        
    if x ==50 and y>=y_coord+200 and y<=y_coord+300:
        x_offset=x_offset*(-1)
        x=x+x_offset
        y_offset=y_offset*(-1)
        y=y+y_offset
    elif x ==50 and y>=y_coord+200 and y<=y_coord+300:

        x_offset=x_offset*(-1)
        x=x+x_offset
        y_offset=y_offset*(-1)
        y=y+y_offset



    
#x=baddle  and bally>=baddle_y top and bally<=baddley down.

        
#counting score
        #if x==51 or y in range(200,300):
            #score1=score1-1
            #x=350
            #y=250
        
        
        #elif x==624 or y in range(200,300):
            #score2=score2-1
            #x=350
            #y=250
        



    


    
    
        
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here

    pygame.draw.rect(screen,WHITE,[x,y,25,10],1)
    pygame.draw.rect(screen,RED,[0,0,50,50],1)
    
    pygame.draw.rect(screen,RED,[650,200,50,100],1)
    pygame.draw.rect(screen,RED,[0,200+y_coord,50,100],1)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text1 = font.render(str(score1),True,RED)
    text2 = font.render(str(score2),True,RED)
    screen.blit(text1, [150, 50])
    screen.blit(text2, [500, 50])
    
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
