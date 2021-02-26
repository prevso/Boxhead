import background
import player
import pygame
import zombie
import random
import bullet
import die
import time
# import game
import score
# from pygame.locals import *             #단순 import 보다 속도가 빠름
from interface import *    # 이렇게 쓰면 interface.keyboard 라고 안써도 된다


player1 = player.Player()
zombie1 = zombie.Zombie(random.randint(0, 1400), random.randint(0, 800), 1)
score1 = score.Score()
running = True
zombies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
# help (zombies)
FPS = 120
default_font = pygame.font.Font('NanumGothic.ttf', 40)
YELLOW = (250, 250, 50)
while running:
    fps_clock = pygame.time.Clock()

    # pygame.mixer.music.load('bgm.mp3')
    # pygame.mixer.music.play(-1)
    if random.randint(1, 30) == 1:
        zombie1 = zombie.Zombie(random.randint(player1.rect.width + 10, 500) + player1.rect.x,
                                random.randint(player1.rect.height + 100, 500) + player1.rect.y, 2+score1.kill_score*0.1) \
                  or zombie.Zombie(random.randint(player1.rect.width - 10, -500) + player1.rect.x,
                                   random.randint(player1.rect.height - 100, - 500) + player1.rect.y, 2+score1.kill_score*0.1)
        zombies.add(zombie1)

    background.screen.blit(background.background, (0, 0))  # 배경 그리기
    command1 = keyboard()

    print(command1)
    if command1 == 'key_quit':
        running = False

    if command1 == 'key_left':
        player1.dx = player1.dx - 7
        player1.theta = 180
    if command1 == 'key_right':
        player1.dx = player1.dx + 7
        player1.theta = 0
    if command1 == 'key_up':
        player1.dy = player1.dy - 7
        player1.theta = 90
    if command1 == 'key_down':
        player1.dy = player1.dy + 7
        player1.theta = 270
    if command1 == 'key_space':
        bullet1 = bullet.Bullet(player1.rect.x + player1.rect.width / 2, player1.rect.y + player1.rect.height / 2, 30, player1)
        bullets.add(bullet1)
        bullet1.sound.play()
    if command1 == 'key_stop_x':
        player1.dx = 0
    if command1 == 'key_stop_y':
        player1.dy = 0
    if command1 == 'key_all_stop':
        player1.dx = 0
        player1.dy = 0
    print('--')
    print(command1)

    score1.draw_text('KILL SCORE: {}'.format(score1.kill_score),default_font, background.screen, 200, 20, YELLOW)

    if pygame.sprite.spritecollide(player1, zombies, True):

        die.die2(background.screen, player1.rect.x + player1.rect.width/2, player1.rect.y+player1.rect.height/2)
        player1.kill()
        default_font= pygame.font.Font('NanumGothic.ttf', 200)

        score1.draw_text('FINAL SCORE: {}'.format(score1.kill_score), default_font, background.screen,
                             background.screen_width / 2, background.screen_height / 2, YELLOW)
        pygame.display.update()
        pygame.time.wait(2000)
        running = False



    for bullet1 in bullets:
        zombie1 = bullet1.collide(zombies)
        if zombie1:
            bullet1.kill()
            zombie1.kill()
            die.die1(background.screen, zombie1.rect.x + zombie1.rect.width/2, zombie1.rect.y + zombie1.rect.height/2)
            score1.kill_score += 1

    bullets.update()
    bullets.draw(background.screen)
    # print(bullets)

    player1.player_moving()
    player1.draw(background.screen)

    zombies.update(player1.rect.x, player1.rect.y)
    zombies.draw(background.screen)

    pygame.display.update()     #게임 화면을 다시 그리기

    fps_clock.tick(FPS)

