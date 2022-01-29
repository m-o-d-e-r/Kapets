import sys
from source.Config.config import (
        WINDOW_SIZE, WIDTH, HEIGHT, RUN,
        FPS, BORDER, WIDTH_K, HEIGHT_K,
        UserEvents
)
from pygame.locals import *
import pygame
from source.Config.root_path import BasePath
from source.menu import (
    GameMenu, Menu, Datas,
    SettingsMenu, LanguageMenu
)
from source.components import Components
from source.Core.core import MainCore
 

pygame.display.init()
pygame.font.init()
pygame.init()

OPENGL_IS_ACTIVE = False
#try:
#    flags_ = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.OPENGL

#    window = pygame.display.set_mode((0,0), flags_)
#    window.set_alpha(None)
#except:
#    flags_ = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE

#    window = pygame.display.set_mode((0,0), flags_)
#    window.set_alpha(None)
#else:
#    OPENGL_IS_ACTIVE = True
flags_ = pygame.FULLSCREEN #| pygame.DOUBLEBUF | pygame.HWSURFACE

window = pygame.display.set_mode((0,0), flags_)
window.set_alpha(None)



clock = pygame.time.Clock()
pygame.mouse.set_visible(False) # прибрати курсор



Components.init() # Ініціалізація компонентів гри (Гравець, Вороги, Бос)

player = Components.PLAYER_
enemis = Components.ENEMIS_
bos = next(Components.BOS_LIST)
#bos = Components.BOS_


pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.time.set_timer(UserEvents.TELEPORT_DELAY, 100)
pygame.time.set_timer(UserEvents.BOS_ANIMATION, 200)
pygame.time.set_timer(UserEvents.PLAYER_ANIMATION, 80)
pygame.time.set_timer(UserEvents.SHOOT, 100)


Datas.setData((WIDTH_K, HEIGHT_K, WIDTH))
menu = Menu(WIDTH, HEIGHT, f"{BasePath.IMAGES_DIR}/menu/fon/fon3.png")
#menu.add_button("continue", "images/menu/main_menu/continueD.png")
menu.add_button("new_game", "images/menu/main_menu/newgameD.png")
menu.add_button("settings", "images/menu/main_menu/settingsD.png")
menu.add_button("exit", "images/menu/main_menu/exitD.png")


settingsMenu = SettingsMenu(WIDTH, HEIGHT)
settingsMenu.add_button("game", "images\menu\settings\game\gameD.png")
settingsMenu.add_button("control", "images\menu\settings\control\controlD.png")
settingsMenu.add_button("language", "images\menu\settings\language\languageD.png")


languageMenu = LanguageMenu(WIDTH, HEIGHT)
languageMenu.add_button("rusian", r"images\menu\settings\language\ruD.png")
languageMenu.add_button("english", "images\menu\settings\language\enD.png")


gameMenu = GameMenu(WIDTH, HEIGHT)
gameMenu.add_button("music", "images\menu\settings\game\music\music0.png")
gameMenu.add_button("effect", "images\menu\settings\game\effect\effect0.png")



MainCore_ = MainCore(window, player, bos, enemis, menu, settingsMenu, languageMenu, gameMenu, clock)


if __name__ == "__main__":
    MainCore_.ExtendVariables("OPENGL_IS_ACTIVE", OPENGL_IS_ACTIVE)
    MainCore_.ExtendVariables("menu", menu)
    MainCore_.ExtendVariables("settingsMenu", settingsMenu)
    MainCore_.ExtendVariables("languageMenu", languageMenu)
    MainCore_.ExtendVariables("gameMenu", gameMenu)

    MainCore.SetEventHandler()

    MainCore_.RunGame()
