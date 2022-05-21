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
            

player1 = Player("racket.png", 5, win_height/3.5, 3, 50, 200, pygame.K_w, pygame.K_s)
player2 = Player("racket.png", win_width-50, win_height/3.5, 3, 50, 200, pygame.K_UP, pygame.K_DOWN)

ball = GameSprite("ball.png", win_width/2.25+20, win_height/2.5, 2, 50, 50)

dx = 3
dy = 3
pygame.font.init()
font = pygame.font.SysFont("Arial", 40)
pass1 = font.render("Player 1 пропустил мяч", True, (255,215,0))
pass2 = font.render("Player 2 пропустил мяч", True, (255,215,0))

pass_player1 = 0
pass_player2 = 0




clock = pygame.time.Clock()
FPS = 60

game = True

Countdown = True
start = timer()
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
    if Countdown:
        finish = timer()
        сountdown = 3 - int(finish - start)  
        if сountdown == 0:
            finish = False
            Countdown = False
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
            win_display.blit(pass1,(100,100))
            pass_player2 += 1
            finish = True
            Countdown = True

        if ball.rect.x > player2.rect.x:
            win_display.blit(pass2,(100,100))
            pass_player1 += 1
            finish = True
            Countdown = True

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False             
    clock.tick(FPS)
    pygame.display.update()
