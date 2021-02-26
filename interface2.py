import background
import player
import pygame
import zombie
import random
import bullet
import die
import time
import game
# from pygame.locals import *             #단순 import 보다 속도가 빠름


class Keyboard:
    def __init__(self):
        self.quit = False
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False



    def kchecking(self):

        for event in pygame.event.get():         #어떤 이벤트가 발생 하였는가
            if event.type == pygame.QUIT:        #창을 닫히는 이벤트가 발생하였는가?
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Keyboard.left = True
                elif event.key == pygame.K_RIGHT:
                    Keyboard.right = True
                elif event.key == pygame.K_UP:
                    Keyboard.up = True
                elif event.key == pygame.K_DOWN:
                 Keyboard.right = True
                elif event.key == pygame.K_SPACE:
                    Keyboard.space = True



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Keyboard.left = False
                elif event.key == pygame.K_RIGHT:
                    Keyboard.right = False
                elif event.key == pygame.K_DOWN:
                    Keyboard.down = False
                elif event.key == pygame.K_UP:
                    Keyboard.up = False
                elif event.key == pygame.K_SPACE:
                    Keyboard.space = False




