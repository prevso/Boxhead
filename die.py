import pygame
#die.py를 따로 만들어야하는 이유: 안그러면 player1을 kill 했을 때 이미지가 같이 사라지게 된다.

def die1(surface, x, y):
    die_image = pygame.image.load('explosion.png')
    die_rect = die_image.get_rect()
    die_rect.x = x
    die_rect.y = y
    surface.blit(die_image, die_rect)
    die1_sound = pygame.mixer.Sound('die_zombie.wav')
    die1_sound.play()

def die2(surface, x, y):
    # die_image = pygame.image.load('blood.png')
    # die_rect = die_image.get_rect()
    # die_rect.x = x
    # die_rect.y = y
    # surface.blit(die_image, die_rect)
    die2_sound = pygame.mixer.Sound('die_player.wav')
    die2_sound.play()

