
import pygame

def keyboard():
    global command

    for event in pygame.event.get():         #어떤 이벤트가 발생 하였는가
        if event.type == pygame.QUIT:        #창을 닫히는 이벤트가 발생하였는가?
            command = 'key_quit'
            return 'key_quit'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                command = 'key_left'
                return 'key_left'
            elif event.key == pygame.K_RIGHT:
                command = 'key_right'
                return 'key_right'
            elif event.key == pygame.K_UP:
                command = 'key_up'
                return 'key_up'
            elif event.key == pygame.K_DOWN:
                command = 'key_down'
                return 'key_down'
            elif event.key == pygame.K_SPACE:
                command = 'key_space'
                return 'key_space'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                return 'key_stop_x'
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                return 'key_stop_y'





