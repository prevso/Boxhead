import pygame
import background
import time
import player

class Zombie(pygame.sprite.Sprite, player.Player):
    def __init__(self, xpos, ypos, speed):
        super().__init__()
        self.image = pygame.image.load('zombie.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self, playerx, playery):
        if playerx - self.rect.x > 0:
            self.rect.x = self.rect.x + self.speed
        else:
            self.rect.x = self.rect.x - self.speed

        if playery - self.rect.y > 0:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = self.rect.y - self.speed



        # if self.rect.x < 0 or self.rect.x + self.rect.width > background.screen_width:
        #     self.rect.x -= self.dx
        #
        # if self.rect.y < 0 or self.rect.y + self.rect.height > background.screen_height:
        #     self.rect.y -= self.dy

    def draw(self, screen):
        #rotated


        screen.blit(self.image, self.rect)
        # print('drawz')




    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite

    # def explode(self, screen):
    #     screen.blit(self.die_image, self.die_image.get_rect())

        # for i in range (600):
        #     self.draw(background.screen)
        #     i += 1
        # self.kill()