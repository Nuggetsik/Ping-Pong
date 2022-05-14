import pygame

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
            if self.rect.y > -20:
                self.rect.y -= self.speed
        elif keys_pressed[self.b_d]:
            if self.rect.y < win_height - 125:
                self.rect.y += self.speed
            

player1 = Player("racket.png", 5, win_height/3.5, 3, 50, 200, pygame.K_w, pygame.K_s)
player2 = Player("racket.png", win_width-50, win_height/3.5, 3, 50, 200, pygame.K_UP, pygame.K_DOWN)

ball = GameSprite("ball.png", win_width/2.25+20, win_height/2.5, 2, 50, 50)

clock = pygame.time.Clock()
FPS = 60

game = True

while game:
    win_display.blit(background, (0, 0))
    #отображение спрайтов-игроков
    player1.reset()
    player2.reset()
    ball.reset()
    #перемещение спрайтов-игроков
    player1.update()
    player2.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        
                
    clock.tick(FPS)
    pygame.display.update()
