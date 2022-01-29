import math
from numpy.lib.type_check import asscalar
import pygame
import random

from pygame.locals import Color

from .Config.config import HEIGHT_K, WIDTH, HEIGHT, BORDER, Colors, WIDTH_K, draw
from .Config.root_path import BasePath


import numpy


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 3
        self.height = 3

        self.speed = random.uniform(3, 5)

    def draw(self, window, pos):
        if math.sqrt((pos[0] - self.x) * (pos[0] - self.x) + (pos[1] - self.y) * (pos[1] - self.y)) > 100:
            pygame.draw.rect(window, (255, random.randint(20, 200), 0), (self.x, self.y, self.width, self.height))

        radians = math.atan2((self.y - pos[1]),(self.x - pos[0]))
        dy1 = math.sin(radians) * self.speed
        dx1 = math.cos(radians) * self.speed
        self.x -= dx1
        self.y -= dy1

    @staticmethod
    def draw2(window, pos, datas):
        if math.sqrt((pos[0] - datas[0]) * (pos[0] - datas[0]) + (pos[1] - datas[1]) * (pos[1] - datas[1])) > 100:
            pygame.draw.rect(window, (255, random.randint(20, 200), 0), (datas[0], datas[1], 3, 3))


        radians = math.atan2((datas[1] - pos[1]), (datas[0] - pos[0]))
        dy1 = math.sin(radians) * datas[2]
        dx1 = math.cos(radians) * datas[2]
        datas[0] -= dx1
        datas[1] -= dy1

        return datas


class ParticleC:
    def __init__(self):
        self.speed = random.uniform(3, 4) * random.choice((-1, 1))


        self.R = random.randint(65, 100)
        self.i = 0
        self.a = 100
        self.b = 100

    def draw(self, window, x, y):
        angle = self.i * math.pi / 180

        l = int(math.acos((self.a - 400) / math.sqrt(500 * 500 - 400 * 400)))

        a = (self.R * math.cos(angle + l)) + x
        b = (self.R * math.sin(angle + l)) + y

        self.i += self.speed

        pygame.draw.rect(window, Colors.GREEN, (a, b, 5, 5))

    @staticmethod
    def draw2(window, x, y, datas): #datas -> [speed, R, i, a, b]
        angle = datas[2] * math.pi / 180

        l = int(math.acos((datas[3] - 400) / math.sqrt(500 * 500 - 400 * 400)))

        a = (datas[1] * math.cos(angle + l)) + x
        b = (datas[1] * math.sin(angle + l)) + y

        datas[2] += datas[0]

        pygame.draw.rect(window, Colors.GREEN, (a, b, 5, 5))

        return datas


class PlayerAnimationInj:
    __slots__ = (
        "waiting_animation", "waiting_animation_images",
        "up_animation", "up_animation_images",
        "right_animation", "right_animation_images",
        "down_animation", "down_animation_images",
        "left_animation", "left_animation_images",
        "dr_animation", "dr_animation_images",
        "dl_animation", "dl_animation_images",
        "ur_animation", "ur_animation_images",
        "ul_animation", "ul_animation_images"
    )

    def __init__(self):
        self.waiting_animation = 0
        self.waiting_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/waiting/waiting1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/waiting/waiting2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]

        self.up_animation = 0
        self.up_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/up/up1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/up/up2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]

        self.right_animation = 0
        self.right_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/right/right1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/right/right2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]

        self.down_animation = 0
        self.down_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/down/down1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/down/down2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]

        self.left_animation = 0
        self.left_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/left/left1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/left/left2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]


        self.dr_animation = 0
        self.dr_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/dr/dr1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/dr/dr2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]

        self.dl_animation = 0
        self.dl_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/dl/dl1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/dl/dl2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]

        self.ur_animation = 0
        self.ur_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/ur/ur1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/ur/ur2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]

        self.ul_animation = 0
        self.ul_animation_images = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/ul/ul1.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/player_inj/ul/ul2.png').convert_alpha(), (Player.K, Player.K)).convert_alpha(),
        ]


    def waiting_animation_foo(self, window, pos, pl):
        self.waiting_animation += 1
        if self.waiting_animation >= 15:
            self.waiting_animation = 0
            pl.inj = False


        window.blit(
            self.waiting_animation_images[self.waiting_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

    def up_animation_foo(self, window, pos, pl):
        self.up_animation += 1
        if self.up_animation >= 15:
            self.up_animation = 0
            pl.inj = False

        window.blit(
            self.up_animation_images[self.up_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

    def right_animation_foo(self, window, pos, pl):
        self.right_animation += 1
        if self.right_animation >= 15:
            self.right_animation = 0
            pl.inj = False

        window.blit(
            self.right_animation_images[self.right_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

    def down_animation_foo(self, window, pos, pl):
        self.down_animation += 1
        if self.down_animation >= 15:
            self.down_animation = 0
            pl.inj = False

        window.blit(
            self.down_animation_images[self.down_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

    def left_animation_foo(self, window, pos, pl):
        self.left_animation += 1
        if self.left_animation >= 15:
            self.left_animation = 0
            pl.inj = False

        window.blit(
            self.left_animation_images[self.left_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

    def dr_animation_foo(self, window, pos, pl):
        self.dr_animation += 1
        if self.dr_animation >= 15:
            self.dr_animation = 0
            pl.inj = False

        window.blit(
            self.dr_animation_images[self.dr_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

    def dl_animation_foo(self, window, pos, pl):
        self.dl_animation += 1
        if self.dl_animation >= 15:
            self.dl_animation = 0
            pl.inj = False

        window.blit(
            self.dl_animation_images[self.dl_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

    def ur_animation_foo(self, window, pos, pl):
        self.ur_animation += 1
        if self.ur_animation >= 15:
            self.ur_animation = 0
            pl.inj = False

        window.blit(
            self.ur_animation_images[self.ur_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

    def ul_animation_foo(self, window, pos, pl):
        self.ul_animation += 1
        if self.ul_animation >= 15:
            self.ul_animation = 0
            pl.inj = False

        window.blit(
            self.ul_animation_images[self.ul_animation // 8],
            (pos[0] - Player.K // 4, pos[1] - Player.K // 4)
            )

class PlayerAnimation:
    CHANGE_FRAME_FLAG = False

    ISTELEPORT = False
    TELEPORTFRAME = 1
    TELEPORTSET = {
        1 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/teleport/1.png'), (37 * int(WIDTH_K), 37 * int(WIDTH_K))),
        2 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/teleport/2.png'), (37 * int(WIDTH_K), 37 * int(WIDTH_K))),
        3 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/teleport/3.png'), (37 * int(WIDTH_K), 37 * int(WIDTH_K))),
        4 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/teleport/4.png'), (37 * int(WIDTH_K), 37 * int(WIDTH_K)))
    }

    def __init__(self, player):
        self.ANIMATION_FRAME = 1
        self.CURRENT_FRAME = None
        self.LAST_MOVEMENT = -1
        self.CURRENT_MOVEMENT = 0

        self.DATASET = {
            -1 : ([(f'{BasePath.IMAGES_DIR}/waiting/pl.png'), 1] for i in range(1, 5)),
            0 : ([(f'{BasePath.IMAGES_DIR}\\up\\up{i}.png'), 1] for i in range(1, 5)),
            1 : ([(f'{BasePath.IMAGES_DIR}\\right\\right{i}.png'), 1] for i in range(1, 5)),
            2 : ([(f'{BasePath.IMAGES_DIR}\\down\\down{i}.png'), 1] for i in range(1, 5)),
            3 : ([(f'{BasePath.IMAGES_DIR}\\left\\left{i}.png'), 1] for i in range(1, 5)),
            4 : f'{BasePath.IMAGES_DIR}/down_right/dr.png',
            5 : f'{BasePath.IMAGES_DIR}/down_left/dl.png',
            6 : f'{BasePath.IMAGES_DIR}/up_right/ur.png',
            7 : f'{BasePath.IMAGES_DIR}/up_left/ul.png'
        }

        self.LAST_FRAME_DATASET = {
            -1 : f'{BasePath.IMAGES_DIR}/waiting/pl.png',
            0 : f'{BasePath.IMAGES_DIR}\\up\\up3.png',
            1 : f'{BasePath.IMAGES_DIR}\\right\\right3.png',
            2 : f'{BasePath.IMAGES_DIR}\\down\\down3.png',
            3 : f'{BasePath.IMAGES_DIR}\\left\\left3.png',
            4 : f'{BasePath.IMAGES_DIR}/down_right/dr.png',
            5 : f'{BasePath.IMAGES_DIR}/down_left/dl.png',
            6 : f'{BasePath.IMAGES_DIR}/up_right/ur.png',
            7 : f'{BasePath.IMAGES_DIR}/up_left/ul.png'
        }

    def rebut_generators(self, player):
        if player.animation.LAST_MOVEMENT != player.side:
            if player.side == -1:
                player.animation.DATASET[-1] = ([(f'{BasePath.IMAGES_DIR}/waiting/pl.png'), 1] for i in range(1, 5))
            elif player.side == 0:
                player.animation.DATASET[0] = ([(f'{BasePath.IMAGES_DIR}\\up\\up{i}.png'), 1] for i in range(1, 5))
            elif player.side == 1:
                player.animation.DATASET[1] = ([(f'{BasePath.IMAGES_DIR}\\right\\right{i}.png'), 1] for i in range(1, 5))
            elif player.side == 2:
                player.animation.DATASET[2] = ([(f'{BasePath.IMAGES_DIR}\\down\\down{i}.png'), 1] for i in range(1, 5))
            elif player.side == 3:
                player.animation.DATASET[3] = ([(f'{BasePath.IMAGES_DIR}\\left\\left{i}.png'), 1] for i in range(1, 5))
            elif player.side == 4:
                player.animation.DATASET[4] = f'{BasePath.IMAGES_DIR}/down_right/dr.png'
            elif player.side == 5:
                player.animation.DATASET[5] = f'{BasePath.IMAGES_DIR}/down_left/dl.png'
            elif player.side == 6:
                player.animation.DATASET[6] = f'{BasePath.IMAGES_DIR}/up_right/ur.png'
            elif player.side == 7:
                player.animation.DATASET[7] = f'{BasePath.IMAGES_DIR}/up_left/ul.png'

            player.animation.LAST_MOVEMENT = player.side
    
    def draw_last_frame(self, window, player):
        window.blit(
            pygame.transform.scale(
                pygame.image.load(
                    player.animation.LAST_FRAME_DATASET.get(player.side)
                ).convert_alpha(),
                (
                    Player.K, Player.HK
                )
            ).convert_alpha(),
            (
                player.x - Player.K // 4,
                player.y - Player.K // 4,
            )
        )

    def draw_current_frame(self, window, player):
        window.blit(
            pygame.transform.scale(
                pygame.image.load(
                    player.animation.CURRENT_FRAME
                ).convert_alpha(),
                (
                    Player.K, Player.HK
                )
            ).convert_alpha(),
            (
                player.x - Player.K // 4,
                player.y - Player.K // 4,
            )
        )        

ANGLE = 0
class Bullet:
    SPEED = 8
    WIDTH = 30
    HEIGHT = 30
    WK = int(pygame.image.load('images/bullet/1.png').get_rect().width * WIDTH_K)
    HK = int(pygame.image.load('images/bullet/1.png').get_rect().height * HEIGHT_K)
    def __init__(self, x, y):
        self.X = 0
        self.Y = 0
        self.SET = False

        self.USER_AIM = 0

        self.x = x
        self.y = y

        self.SHOOT = False

        self.CURSOR_X = 0
        self.CURSOR_Y = 0

        self.PLAYER_X = 0
        self.PLAYER_Y = 0

        self.set_r = False

        self.image = pygame.image.load('images/bullet/1.png').convert_alpha()
        self.width = Bullet.WK
        self.height = Bullet.HK

class Bomb:
    def __init__(self):
        self.CURSOR_X = 0
        self.CURSOR_Y = 0
        self.PLAYER_X = 0
        self.PLAYER_Y = 0
        self.x = self.PLAYER_X
        self.y = self.PLAYER_Y

        self.speed = 7

class Player:
    K = int(pygame.image.load(f"{BasePath.IMAGES_DIR}\\up\\up1.png").get_rect().width * WIDTH_K)
    HK = int(pygame.image.load(f'{BasePath.IMAGES_DIR}\\up\\up1.png').get_rect().height * HEIGHT_K)
    def __init__(self, x = WIDTH // 2, y = HEIGHT // 2):
        self.shoot_ = False

        self.shoot_bomb_ = False

        self.spawn = False

        self.x = x
        self.y = y
        self.width = int(Player.K * 0.5)
        self.height = int(Player.K * 0.5)

        self.speed = 5

        self.XP = 10

        self.side = -1

        self.image = ""

        self.npparticles = numpy.array([0 for i in range(20)], dtype = object)
        for num, item in enumerate(self.npparticles):
            self.npparticles[num] = [self.x, self.y, random.uniform(3, 5)]

        self.npparticles2 = numpy.array([0 for i in range(5)], dtype = object)
        for num, item in enumerate(self.npparticles2):
            self.npparticles2[num] = [
                random.uniform(2, 4) * random.choice((-1, 1)),
                random.randint(70, 100), 100, 100
            ]

        self.bullets = [Bullet(self.x, self.y) for i in range(30)]#        self.npbullets = numpy.empty(30, dtype = object)



        self.bomb_ = Bomb()

        self.inj = False
        self.inj_animation = PlayerAnimationInj()
        self.animation = PlayerAnimation(self)

        self.teleport_procces = False

        self.cursor = pygame.transform.scale(pygame.image.load("images/menu/cursor/cursor.png"), tuple(map(int, (50 * WIDTH_K, 50 * WIDTH_K))))

    def draw(self, window):

        if self.spawn:
            for num, particle in enumerate(self.npparticles):
                self.npparticles[num] = Particle.draw2(
                    window,
                    [
                        random.randint(self.x - 50, self.x + self.width + 50),
                        random.randint(self.y - 50, self.y + self.height + 50)
                    ],
                    particle
                )

            for num, particle in enumerate(self.npparticles2):
                self.npparticles2[num] = ParticleC.draw2(
                    window, self.x + self.width // 2, self.y + self.height // 2, particle
                )

            if not self.inj:
                if not self.teleport_procces:
                    self.animation.rebut_generators(self)

                    if self.animation.ANIMATION_FRAME < 5:
                        if PlayerAnimation.CHANGE_FRAME_FLAG:
                            try:
                                self.animation.CURRENT_FRAME = next(self.animation.DATASET.get(self.side))[0]
                            except:
                                self.animation.draw_last_frame(window, self)

                            self.animation.ANIMATION_FRAME += 1

                            PlayerAnimation.CHANGE_FRAME_FLAG = False

                        try:
                            self.animation.draw_current_frame(window, self)
                        except:
                            ...
                    else:
                        self.animation.draw_last_frame(window, self)

                        self.animation.ANIMATION_FRAME = 1

            else:
                if self.side == -1:
                    self.inj_animation.waiting_animation_foo(window, [self.x, self.y], self)
                elif self.side == 0x0:
                    self.inj_animation.up_animation_foo(window, [self.x, self.y], self)
                elif self.side == 0x1:
                    self.inj_animation.right_animation_foo(window, [self.x, self.y], self)
                elif self.side == 0x2:
                    self.inj_animation.down_animation_foo(window, [self.x, self.y], self)
                elif self.side == 0x3:
                    self.inj_animation.left_animation_foo(window, [self.x, self.y], self)
                elif self.side == 0x4:
                    self.inj_animation.dr_animation_foo(window, [self.x, self.y], self)
                elif self.side == 0x5:
                    self.inj_animation.dl_animation_foo(window, [self.x, self.y], self)
                elif self.side == 0x6:
                    self.inj_animation.ur_animation_foo(window, [self.x, self.y], self)
                elif self.side == 0x7:
                    self.inj_animation.ul_animation_foo(window, [self.x, self.y], self)

    def controle(self, keys, ticks):
        key = 0
        key_list = []
        if keys[pygame.K_w] and self.y > BORDER:
            self.y -= int(self.speed * ticks)
            self.side = 0x0
            key += 1
            key_list.append("w")
        if keys[pygame.K_d] and self.x < WIDTH - BORDER - self.width:
            self.x += int(self.speed * ticks)
            self.side = 0x1
            key += 1
            key_list.append("d")
        if keys[pygame.K_s] and self.y < HEIGHT - BORDER - self.height:
            self.y += int(self.speed * ticks)
            self.side = 0x2
            key += 1
            key_list.append("s")
        if keys[pygame.K_a] and self.x > BORDER:
            self.x -= int(self.speed * ticks)
            self.side = 0x3
            key += 1
            key_list.append("a")

        if key == 0:
            self.side = -1

        if "w" in key_list and "a" in key_list:
            self.side = 0x7
        elif "w" in key_list and "d" in key_list:
            self.side = 0x6
        elif "s" in key_list and "a" in key_list:
            self.side = 0x5
        elif "s" in key_list and "d" in key_list:
            self.side = 0x4

    def aim(self, window, pos):
        window.blit(
            self.cursor,
            (
                pos[0] - self.cursor.get_rect().width // 2,
                pos[1] - self.cursor.get_rect().height // 2
            )
        )

    def shoot(self, window, bos, ticks):
        for num, bullet in enumerate(self.bullets):
            if not bullet.SHOOT:
                bullet.x = self.x
                bullet.y = self.y
            else:
                if not bullet.SET:
                    bullet.X = 2 * bullet.CURSOR_X - bullet.PLAYER_X
                    bullet.Y = 2 * bullet.CURSOR_Y - bullet.PLAYER_Y

                    for i in range(20):
                        if (bullet.X > 0 and bullet.X < WIDTH + 20) or (bullet.Y > 0 and bullet.Y < HEIGHT + 20):
                            bullet.X = 2 * bullet.X - bullet.PLAYER_X
                            bullet.Y = 2 * bullet.Y - bullet.PLAYER_Y
                        else:
                            break

                radians = math.atan2((bullet.y - bullet.Y), (bullet.x - bullet.X))
                dy1 = math.sin(radians) * Bullet.SPEED
                dx1 = math.cos(radians) * Bullet.SPEED
                bullet.x -= dx1 * ticks
                bullet.y -= dy1 * ticks


                if not bullet.set_r:
                    angle = 0
                    if bullet.USER_AIM == 1:
                        angle = math.sin(radians) * 90
                    else:
                        angle = math.sin(radians) * -90 + 180

                    bullet.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/bullet/4.png').convert_alpha(), (Bullet.WK, Bullet.HK)).convert_alpha(), angle)

                    bullet.set_r = True


                #pygame.draw.rect(
                #    window, Colors.RED, (bullet.x, bullet.y, bullet.width, bullet.height)
                #)
                window.blit(
                    bullet.image,
                    (
                        bullet.x,
                        bullet.y
                    )
                )

                if bullet.x > WIDTH or bullet.x < 0:
                    self.bullets[num] = Bullet(self.x, self.y)

                if bullet.y > HEIGHT or bullet.y < 0:
                    self.bullets[num] = Bullet(self.x, self.y)


                if not bos.IS_DIE and not bos.HIDDE:
                    pl = pygame.Rect(
                            (bullet.x, bullet.y),
                            (Bullet.WIDTH, Bullet.HEIGHT)
                        )
                    en = pygame.Rect(
                        (bos.x, bos.y),
                        (bos.width, bos.height)
                    )

                    if pl.colliderect(en) == 1:
                        bos.XP -= 1
                        self.bullets[num] = Bullet(self.x, self.y)

                        act = random.choice((1, 0))

                        
                        if act == 1:
                            bos.START = True
                            bos.ISTELEPORT = True
                            bos.teleport_procces = True
                        else:
                            bos.inj = True

    def bomb_activate(self, window):
        if self.shoot_bomb_:

            if (self.bomb_.x != self.bomb_.CURSOR_X) and (self.bomb_.y != self.bomb_.CURSOR_Y):
                pygame.draw.rect(window, Colors.RED,
                    (
                        self.bomb_.x, self.bomb_.y,
                        100, 100
                    )
                )


                radians = math.atan2(
                    (
                        self.bomb_.PLAYER_Y - self.bomb_.CURSOR_Y
                    ),
                    (
                        self.bomb_.PLAYER_X - self.bomb_.CURSOR_X
                    )
                )
                dy1 = math.sin(radians) * self.bomb_.speed
                dx1 = math.cos(radians) * self.bomb_.speed
                self.bomb_.x -= dx1
                self.bomb_.y -= dy1
            else:
                self.shoot_bomb_ = False
