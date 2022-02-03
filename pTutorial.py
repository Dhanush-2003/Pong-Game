#Imports
import pygame

#Initialize all imported pygame modules
pygame.init()

#Initialize a window or screen for display
win  = pygame.display.set_mode((750,500))

#Display Title is named Pong
pygame.display.set_caption("Pong")

#FFFFFF Hex Color | RGB: 255, 255, 255 | WHITE
white = (255, 255, 255) 

#000000 Hex Color | RGB: 0, 0, 0 | BLACK
black = (0, 0, 0)

#Features for Paddle Class
class Paddle(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0
        self.speed = 10
        
#Features for Ball Class
class Ball(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 15
        self.dx = 1
        self.dy = 1

#Coordinates for Paddle 1
paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

#Coordinates for Paddle 2
paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

#paddle_speed = 10

#Coordinates for Pong Ball
ball = Ball()
ball.rect.x = 375
ball.rect.y = 225

#Grouping all the variables made into one variable
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)

#The display we are trying to draw on
def redraw():
    win.fill(black)
    #Title Font
    font = pygame.font.SysFont("Comic Sans MS", 30)
    text =  font.render("PONG", False, white)
    textRect = text.get_rect()
    textRect.center = (750//2, 25)
    
    #Player 1 Score
    p1_score = font.render(str(paddle1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)
   
    #Player 2 Score
    p2_score = font.render(str(paddle2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)

    win.blit(text, textRect)
    all_sprites.draw(win)
    pygame.display.update()


run = True


#Setting up main loop for the game

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        #If you want to exit the game, run is set to false to end the game
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    
    #Paddle Movement, player 1 and player 2 keys are set
    if key [pygame.K_w]:
        paddle1.rect.y -= paddle1.speed 
    if key [pygame.K_s]:
        paddle1.rect.y += paddle1.speed 
    if key [pygame.K_UP]:
        paddle2.rect.y -= paddle2.speed   
    if key [pygame.K_DOWN]:
        paddle2.rect.y += paddle2.speed
    
    #Speed of the Pong Ball 
    ball.rect.x += ball.speed * ball.dx
    ball.rect.y += ball.speed * ball.dy

    #Checking collision for the bottom of the screen
    if ball.rect.y > 490:
        ball.dy = -1
    
    #Checking collision for the right of the screen
    if ball.rect.x > 740:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = -1
        paddle1.points += 1
    
    #Checking collision for the top of the screen
    if ball.rect.y < 10:
        ball.dy = 1
    
    #Checking collision for the left of the screen
    if ball.rect.x < 10:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = 1
        paddle2.points += 1

    #Checking collision for the first paddle
    if paddle1.rect.colliderect(ball.rect):
        ball.dx = 1

    #Checking collision for the second paddle
    if paddle2.rect.colliderect(ball.rect):
        ball.dx = -1    

    
    redraw()

pygame.quit()
