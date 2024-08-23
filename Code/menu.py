#!/usr/bin/python
# -*- coding: utf-8 -*-
from _curses import COLOR_YELLOW, COLOR_WHITE
from idlelib import window

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font


from Code.Const import WIN_WIDTH, COLOR_ORANGE


class Menu:
    def __init__(self, Window):
        self.window = Window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self,):
        menu_option = 1
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size= 50, text= "Mountain", text_color= COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2),70))
            self.menu_text(text_size= 50, text= "Shooter", text_color= COLOR_ORANGE, text_center_pos= ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, MENU_OPTION[i], text_color=COLOR_YELLOW, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(text_size=20, MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

        # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit()  #end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text,True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)




