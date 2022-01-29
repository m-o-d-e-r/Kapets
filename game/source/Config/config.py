import random
#from source.components import Components
from ..menu import *
import pygame
from tkinter import Tk
import numpy
from .root_path import BasePath


w = Tk().winfo_screenwidth()
h = Tk().winfo_screenheight()


RUN = True
WINDOW_SIZE = WIDTH, HEIGHT = (w, h)
BORDER = 5
FPS = 160


WIDTH_K, HEIGHT_K = (
    WIDTH / 320,
    HEIGHT / 180
)


class Timer:
    TIMER = 0

class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

class AnimationControle:
    BOS_K = 0
    BOS_INJ_K = 0
    PLAYER_K = 0


def draw(s, cls_, window, pos, ticks):
    if not cls_.IS_DIE:
        cls_.x += cls_.speedX * ticks
        cls_.y += cls_.speedY * ticks

    if not cls_.inj and not cls_.IS_DIE and not cls_.HIDDE:
        if not cls_.teleport_procces:
            if cls_.speedX > 0 and cls_.speedY > 0:
                cls_.ANIMATION = [
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/dr.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/dr.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/dr.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/dr.png'), (cls_.K, cls_.K))
                ]
            elif cls_.speedX < 0 and cls_.speedY < 0:
                cls_.ANIMATION = [
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/ul.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/ul.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/ul.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/ul.png'), (cls_.K, cls_.K))
                ]
            elif cls_.speedX > 0 and cls_.speedY < 0:
                cls_.ANIMATION = [
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/ur.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/ur.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/ur.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/ur.png'), (cls_.K, cls_.K))
                ]
            elif cls_.speedX < 0 and cls_.speedY > 0:
                cls_.ANIMATION = [
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/dl.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/dl.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/dl.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/dl.png'), (cls_.K, cls_.K))
                ]
            elif cls_.speedX == 0 and cls_.speedY > 0:
                cls_.ANIMATION = [
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/down.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/down.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/down.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/down.png'), (cls_.K, cls_.K))
                ]
            elif cls_.speedX == 0 and cls_.speedY < 0:
                cls_.ANIMATION = [
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/up.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/up.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/up.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/up.png'), (cls_.K, cls_.K))
                ]
            elif cls_.speedX < 0 and cls_.speedY == 0:
                cls_.ANIMATION = [
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/left.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/left.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/left.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/left.png'), (cls_.K, cls_.K))
                ]
            elif cls_.speedX > 0 and cls_.speedY == 0:
                cls_.ANIMATION = [
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/right.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/right.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/right.png'), (cls_.K, cls_.K)),
                    pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/right.png'), (cls_.K, cls_.K))
                ]

            window.blit(
                cls_.ANIMATION[AnimationControle.BOS_K],
                (
                    cls_.x - cls_.width // 2,
                    cls_.y - cls_.height // 2
                )
            )
            window.blit(cls_.head,
                (
                    cls_.x - cls_.width // 2 - 3,
                    cls_.y - cls_.height // 2
                )
            )
    elif cls_.inj and cls_.XP >= 1:
        if cls_.speedX > 0 and cls_.speedY > 0:
            cls_.ANIMATION = [
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/dr/dr1.png'), (cls_.K, cls_.K)),
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/dr/dr2.png'), (cls_.K, cls_.K))
            ]
        elif cls_.speedX < 0 and cls_.speedY < 0:
            cls_.ANIMATION = [
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/ul/ul1.png'), (cls_.K, cls_.K)),
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/ul/ul2.png'), (cls_.K, cls_.K))
            ]
        elif cls_.speedX > 0 and cls_.speedY < 0:
            cls_.ANIMATION = [
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/ur/ur1.png'), (cls_.K, cls_.K)),
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/ur/ur2.png'), (cls_.K, cls_.K))
            ]
        elif cls_.speedX < 0 and cls_.speedY > 0:
            cls_.ANIMATION = [
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/dl/dl1.png'), (cls_.K, cls_.K)),
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/dl/dl2.png'), (cls_.K, cls_.K))
            ]
        elif cls_.speedX == 0 and cls_.speedY > 0:
            cls_.ANIMATION = [
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/down/down1.png'), (cls_.K, cls_.K)),
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/down/down2.png'), (cls_.K, cls_.K)),
            ]
        elif cls_.speedX == 0 and cls_.speedY < 0:
            cls_.ANIMATION = [
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/up/up1.png'), (cls_.K, cls_.K)),
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/up/up2.png'), (cls_.K, cls_.K))
            ]
        elif cls_.speedX < 0 and cls_.speedY == 0:
            cls_.ANIMATION = [
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/left/left1.png'), (cls_.K, cls_.K)),
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/left/left2.png'), (cls_.K, cls_.K)),
            ]
        elif cls_.speedX > 0 and cls_.speedY == 0:
            cls_.ANIMATION = [
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/right/right1.png'), (cls_.K, cls_.K)),
                pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_inj/right/right2.png'), (cls_.K, cls_.K))
            ]

        window.blit(
            cls_.ANIMATION[AnimationControle.BOS_INJ_K],
            (
                cls_.x - cls_.width // 2,
                cls_.y - cls_.height // 2
            )
        )

        cls_.inj_frame += 1

        if cls_.inj_frame == 10:
            cls_.inj_frame = 1
            cls_.inj = False



    if cls_.x <= 0:
        cls_.speedX = -cls_.speedX
    if cls_.y <= BORDER:
        cls_.speedY = -cls_.speedY

    if cls_.x >= WIDTH - BORDER - cls_.width:
        cls_.speedX = -cls_.speedX
    if cls_.y >= HEIGHT - BORDER - cls_.height:
        cls_.speedY = -cls_.speedY

#    pygame.draw.rect(window, Colors.RED, (cls_.x, cls_.y, cls_.width, cls_.height))


class BasePropertyMetaClass(type):
    def __new__(cls_, name, parents, attr):
        
        attr.update(
            {
                "draw" : draw
            }
        )

        return type(name, parents, attr)


class Text:
    def __init__(self, text, style, size, color):
        font = pygame.font.SysFont(style, size)
        self.textsurface = font.render(text, False, color)

def show_text(window, player_xp, bos_xp, count):
    window.blit(Text(f"XP: {player_xp}", 'Comic Sans MS', 30, (168, 10, 68)).textsurface, (5,0))
    window.blit(Text(f"BOS: {bos_xp}", 'Comic Sans MS', 30, (168, 10, 68)).textsurface, (400,0))
    window.blit(Text(f"Count: {count}", 'Comic Sans MS', 30, (168, 10, 68)).textsurface, (700,0)) 

def show_fps(window, fps):
    window.blit(Text(str(int(fps)), 'Comic Sans MS', 20, (100, 255, 100)).textsurface, (WIDTH - 50, 0))


class UserTeleport:
    X = 0
    Y = 0
    START = False
    TIMEFLAGG = False



class UserEvents:
    TELEPORT_DELAY = pygame.USEREVENT + 1
    BOS_ANIMATION = pygame.USEREVENT + 2
    PLAYER_ANIMATION = pygame.USEREVENT + 3
    SHOOT = pygame.USEREVENT + 5