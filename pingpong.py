import pygame
import time


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
            if self.rect.y > 10:
                self.rect.y -= self.speed
        elif keys_pressed[self.b_d]:
            if self.rect.y < win_height - 135:
                self.rect.y += self.speed
            
player1_x, player1_y = 10, win_height/3.5
player2_x, player2_y = win_width-35, win_height/3.5
ball_x, ball_y = win_width/2.25+20, win_height/2.5

player1 = Player("racket.png", player1_x, player1_y, 3, 25, 125, pygame.K_w, pygame.K_s)
player2 = Player("racket.png", player2_x, player2_y, 3, 25, 125, pygame.K_UP, pygame.K_DOWN)

ball = GameSprite("ball.png", ball_x, ball_y, 2, 50, 50)

def reset_parameters():
    player1.rect.y = player1_y
    player2.rect.y = player2_y
    ball.rect.x, ball.rect.y = ball_x, ball_y
    
pass_player1 = 0
pass_player2 = 0

t = 4

dx = 3
dy = 3

pygame.font.init()
font = pygame.font.SysFont("Arial", 30)
pass1 = font.render("Player 1 пропустил мяч", True, (255,215,0))
pass2 = font.render("Player 2 пропустил мяч", True, (255,215,0))

font1 = pygame.font.SysFont("Helvetica", 50)
win_pl1 = font.render("Player 1 одержал победу", True, (150,215,250))
win_pl2 = font.render("Player 2 одержал победу", True, (150,215,250))

pass_pl1_txt = font.render(str(pass_player1), True, (220, 1, 0))
pass_pl2_txt = font.render(str(pass_player2), True, (220, 1, 0))



clock = pygame.time.Clock()
FPS = 60

game = True
finish = True
сountdown = True

while game:
    win_display.blit(background, (0, 0))
    #отображение спрайтов-игроков
    player1.reset()
    player2.reset()
    ball.reset()
    #перерыв между раундами
    if сountdown:
        while t:
            win_display.blit(background, (0, 0))
            timer = font.render(str(t-1), True, (159,250,150))
            win_display.blit(timer, (390,150))
            
            #отображение спрайтов-игроков
            player1.reset()
            player2.reset()
            ball.reset()

            time.sleep(1)
            t -= 1

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    t = 0
                    сountdown = False  
                    game = False     
                          
            clock.tick(FPS)
            pygame.display.update()
         
        finish = False
        сountdown = False
            
        
    
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
            finish_timer = None
            reset_parameters()
            t = 4
            сountdown = True
            win_display.blit(pass1,(250,170))
            pass_player2 += 1
        
        if ball.rect.x > player2.rect.x:
            finish = True
            finish_timer = None
            reset_parameters()
            t = 4
            сountdown = True
            win_display.blit(pass2,(250,170))
            pass_player1 += 1

    if pass_player1 >= 3:
        win_display.blit(win_pl2, (250, 250))
        finish = True
        сountdown = False

    if pass_player2 >= 3:
        win_display.blit(win_pl1, (250, 250))
        finish = True
        сountdown = False

    pass_pl1_txt = font.render(str(pass_player1), True, (220, 1, 0))
    pass_pl2_txt = font.render(str(pass_player2), True, (220, 1, 0))

    win_display.blit(pass_pl1_txt, (370,0))
    win_display.blit(pass_pl2_txt, (410,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False             
    clock.tick(FPS)
    pygame.display.update()

    
