class Score:
    def __init__(self):
        self.kill_score = 0

    def draw_text(self, text, font, surface, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.centerx = x
        text_rect.centery = y
        surface.blit(text_obj, text_rect)


    def occur_of_zombies(self):
        print('f')


    def spped_of_zomibes(self):
        print('f')