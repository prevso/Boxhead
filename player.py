import pygame
import background


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()         #이게 없으면 충돌감지에서 오류가 나버린다
        # self.image = pygame.image.load('C:/Users/민호/PycharmProjects/minho_boxhead/player.png')
        self.__image = pygame.image.load('player.png')  #굳이 Player의 attribute로 설정할 필요가 있을까 ?
        self.__die_image = pygame.image.load('explosion.png')
        self.__dx = 0
        self.__dy = 0
        self.__rect = self.__image.get_rect()
        self.__rect.x = background.screen_width/2 - self.__rect.width/2
        self.__rect.y = background.screen_height/2 - self.__rect.height/2
        self.__theta = 0
        self.__die = False

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    @dx.setter
    def dx(self, dx):
        self.__dx = dx

    @dy.setter
    def dy(self, dy):
        self.__dy = dy

    @property
    def rect(self):
        return self.__rect

    def set_rect_x(self, rectx):
        self.__rect.x = rectx

    def set_rect_y(self, recty):
        self.__rect.y = recty

    @property
    def theta(self):
        return self.__theta

    @theta.setter
    def theta(self, theta):
        self.__theta = theta

    def player_moving(self):
        self.__rect.x = self.__rect.x + self.__dx
        self.__rect.y = self.__rect.y + self.__dy

        if self.__rect.x < 0 or self.__rect.x + self.__rect.width > background.screen_width:
            self.rect.x -= self.dx

        if self.__rect.y < 0 or self.__rect.y + self.__rect.height > background.screen_height:
            self.__rect.y -= self.__dy

    # @property
    def draw(self, screen):
        #rotated


        screen.blit(self.__image, self.__rect)




    # @property
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite