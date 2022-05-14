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
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            if self.rect.y > 5:
                self.rect.x -= self.speed
        elif keys_pressed[pygame.K_d]:
            if self.rect.y < win_width - 5:
                self.rect.x += self.speed
            


clock = pygame.time.Clock()
FPS = 60
keys_pressed = pygame.key.get_pressed()
game = True

while game:
    win_display.blit(background, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        
                
    clock.tick(FPS)
    pygame.display.update()