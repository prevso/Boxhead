import pygame
import player
import background



class Bullet(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed, player):
        super ().__init__()                   #init이 어떻게 쓰인 걸까
        self.__speed = speed
        self.__theta = player.theta
        if self.__theta == 0:
            self.__image = pygame.image.load('bullet0.png')
        elif self.__theta == 90:
            self.__image = pygame.image.load('bullet90.png')
        elif self.__theta == 180:
            self.__image = pygame.image.load('bullet180.png')
        elif self.__theta == 270:
            self.__image = pygame.image.load('bullet270.png')
        self.__rect = self.__image.get_rect()
        self.__rect.x = xpos
        self.__rect.y = ypos
        self.__sound = pygame.mixer.Sound('explosion04.wav')

    def update(self):
        if self.__theta == 0:
            self.__rect.x += self.__speed
            if self.__rect.x + self.__rect.width > background.screen_width:
                self.kill()
        elif self.__theta == 90:
            self.__rect.y -= self.__speed
            if self.__rect.y + self.__rect.height < 0:
                self.kill()
        elif self.__theta == 180:
            self.__rect.x -= self.__speed
            if self.__rect.x + self.__rect.width < 0:
                self.kill()
        elif self.__theta == 270:
            self.__rect.y += self.__speed
            if self.__rect.y + self.__rect.height > background.screen_height:
                self.kill()


    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite

    @property
    def rect(self):
        return self.__rect

    @property
    def sound(self):
        return self.__sound

    @property
    def image(self):
        return self.__image

    @property
    def theta(self):
        return self.__theta

    @property
    def speed(self):
        return self.__speed