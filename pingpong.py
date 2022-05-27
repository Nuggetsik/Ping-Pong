import pygame
from time import time as timer


win_width = 800
win_height = 500
win_display = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("PingPong")
background = pygame.transform.scale(pygame.image.load("background.png"), (win_width, win_height))

#создание игрового класса
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.player = player_image
        self.width = player_width
        self.height = player_height
        self.image = pygame.transform.scale(pygame.image.load(self.player), (self.width, self.height)) 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        

    def reset(self):
        win_display.blit(self.image, (self.rect.x, self.rect.y))

#класс игрока
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height, button_up, button_down):
        super().__init__(player_image, player_x, player_y, player_speed, player_width, player_height)
        self.b_u = button_up
        self.b_d = button_down
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.b_u]:
            if self.rect.y > -25:
                self.rect.y -= self.speed
        elif keys_pressed[self.b_d]:
            if self.rect.y < win_height - 170:
                self.rect.y += self.speed
            
player1_x, player1_y = 5, win_height/3.5
player2_x, player2_y = win_width-50, win_height/3.5
ball_x, ball_y = win_width/2.25+20, win_height/2.5

player1 = Player("racket.png", player1_x, player1_y, 3, 50, 200, pygame.K_w, pygame.K_s)
player2 = Player("racket.png", player2_x, player2_y, 3, 50, 200, pygame.K_UP, pygame.K_DOWN)

ball = GameSprite("ball.png", ball_x, ball_y, 2, 50, 50)

dx = 3
dy = 3
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)
pass1 = font.render("Player 1 пропустил мяч", True, (255,215,0))
pass2 = font.render("Player 2 пропустил мяч", True, (255,215,0))

font1 = pygame.font.SysFont("Helvetica", 50)
win_pl1 = font.render("Player 1 одержал победу", True, (150,215,250))
win_pl2 = font.render("Player 2 одержал победу", True, (150,215,250))

pass_player1 = 0
pass_player2 = 0




clock = pygame.time.Clock()
FPS = 60

game = True
finish = True
Countdown = True
start_timer = timer()
while game:
    win_display.blit(background, (0, 0))
    #отображение спрайтов-игроков
    player1.reset()
    player2.reset()
    ball.reset()

    pass_pl1_txt = font.render(str(pass_player1), True, (220, 1, 0))
    pass_pl2_txt = font.render(str(pass_player2), True, (220, 1, 0))

    win_display.blit(pass_pl1_txt, (370,0))
    win_display.blit(pass_pl2_txt, (410,0))
    #перерыв между раундами
    if Countdown:
        finish_timer = timer()
        
        сountdown = 3 - int(finish_timer - start_timer)  
        if сountdown == 0:
            player1.rect.y = player1_y
            player2.rect.y = player2_y
            ball.rect.x, ball.rect.y = ball_x, ball_y
            finish = False
            Countdown = False
        if сountdown < 0: 
            del finish_timer
            

        timer_ = font.render(str(сountdown), True, (159,250,150))
        win_display.blit(timer_, (390,150))
    
    if not finish:
        #перемещение спрайтов-игроков
        player1.update()
        player2.update()

        ball.rect.x += dx
        ball.rect.y += dy

        if ball.rect.y < 0:
            dy *= -1
        
        elif ball.rect.y > win_height-50:
            dy *= -1

        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            dx *= -1

        if ball.rect.x < player1.rect.x:
            finish = True
            Countdown = True
            win_display.blit(pass1,(250,250))
            pass_player2 += 1
        
        if ball.rect.x > player2.rect.x:
            finish = True
            Countdown = True
            win_display.blit(pass2,(250,250))
            pass_player1 += 1

        if pass_player1 >= 3:
            win_display.blit(win_pl2, (200, 250))

        if pass_player2 >= 3:
            win_display.blit(win_pl1, (200, 250))


                
            
           

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False             
    clock.tick(FPS)
    pygame.display.update()
