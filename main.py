import pygame
import time
pygame.init()  
pygame.display.set_caption("Pong")  # sets the window title
screen = pygame.display.set_mode((700, 500))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

gameover = False
W = False
S = False
I = False
K = False
direction = [W,S,I,K]

#Paddle logic
p1x = 20
p1y = 200
p2x = 650
p2y = 200
#Ball variable   
bx = 350 #X position
by = 250 #Y position
bVx = 5 #Horizontal speed
bVy = 3 #Vertical speed
#Scores 
p1Score = 0
p2Score = 0
#game loop



while gameover != True: #Gameloop----------------------------
    #event queue
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction[0] = True
            if event.key == pygame.K_s:
                direction[1] = True
            if event.key == pygame.K_i:
                direction[2] = True
            if event.key == pygame.K_k:
                direction[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                direction[0] = False
            if event.key == pygame.K_s:
                direction[1] = False
            if event.key == pygame.K_i:
                direction[2] = False
            if event.key == pygame.K_k:
                direction[3] = False
#Game logic--------------------------------------------
    if direction[0] == True:
        vy1 = -3 
    elif direction[1] == True:
        vy1 = 3
    if direction[2] == True:
        vy2 = -3 
    elif direction[3] == True:
        vy2 = 3 

    else:
        vx = 0   
#Ball movement  
    bx += bVx
    by += bVy

#reflect ball off walls
    if by < 0 or by + 100 > 500:
        bVy *=-1
    if bx + 20 > 700:
        bVx *=-1
        p1Score += 1
    if bx < 0:
        bVx *= -1
        p2Score += 1 #score collision
      
#ball paddle collision  
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
    if bx+20 > p2x and by + 20 > p2y and by < p2y + 100:
        bVx *= -1 
    
 #--------------------
 #screen___________________ 
    screen.fill((0,0,0))

    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (0, 0, 0))
    screen.blit(text, (250, 10))
    text = font.render(str(p2Score), 2, (0, 0, 0))
    screen.blit(text, (420, 10))
    pygame.draw.line(screen, (255, 255, 255), [349, 0], [349, 500], 5)
      
     
    pygame.draw.ellipse(screen,(255,255,255),(bx,by,20,20))
    text = font.render(str(p1Score),1,(255,255,255))
    screen.blit(text,(250,10))
    text = font.render(str(p2Score),1,(255,255,255))
    screen.blit(text,(420,10))
     
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100),1)
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100),2)

    pygame.display.flip()
#--------------------------------------


pygame.quit()
