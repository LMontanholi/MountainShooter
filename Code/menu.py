#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image

from Code.const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # o valor -1 é para que a música sempre recomece
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_BLACK, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_BLACK, ((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont('Open Sans', text_size)
        text_surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)
