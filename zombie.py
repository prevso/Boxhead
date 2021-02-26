import pygame
import background
import time
import player


class Zombie(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super().__init__()
        self.__image = pygame.image.load('zombie.png')
        self.__dx = 0
        self.__dy = 0
        self.__rect = self.image.get_rect()
        self.__rect.x = xpos
        self.__rect.y = ypos
        self.__die = False
        self.__speed = speed

    @property
    def image(self):
        return self.__image

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    @property
    def rect(self):
        return self.__rect

    @property
    def die(self):
        return self.__die

    @property
    def speed(self):
        return self.__speed

    def update(self, playerx, playery):       #Group을 쓰려면 이름 update를 바꿀 수 없다
        if playerx - self.rect.x > 0:
            self.rect.x = self.rect.x + self.speed
        else:
            self.rect.x = self.rect.x - self.speed

        if playery - self.rect.y > 0:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = self.rect.y - self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
