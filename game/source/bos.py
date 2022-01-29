from tkinter.constants import CURRENT
import pygame
import random
import math


from .Config.config import Colors, HEIGHT_K, WIDTH, HEIGHT, BORDER, BasePropertyMetaClass, WIDTH_K
from .Config.root_path import BasePath


class Magic:
    ATTACK = False
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 5
        self.height = 5

        self.speed = random.uniform(2, 5)

        self.activate = False


    def use(self):
        if self.activate:
            self.x -= self.speed

    @staticmethod
    def foo(bos_, window, player):
        if bos_.timer.TIMER == 1 or Magic.ATTACK:
            Magic.ATTACK = True
            for num, magic in enumerate(bos_.all_magic):
                magic.activate = True
                pygame.draw.rect(
                    window, Colors.GREEN,
                    (magic.x, magic.y, magic.width, magic.height)
                )
                magic.use()


                pl = pygame.Rect(
                    (player.x, player.y),
                    (player.width, player.height)
                )
                en = pygame.Rect((magic.x, magic.y), (magic.width, magic.height))

                if not player.teleport_procces:
                    if pl.colliderect(en) == 1:
                        player.XP -= 1
                        player.inj =  True

                        bos_.all_magic.pop(num)

                if magic.x < 0:
                    bos_.all_magic.pop(num)

        else:
            for m in bos_.all_magic:
                m.x = bos_.x + bos_.width - m.width
                m.y = bos_.y + bos_.height - m.height


        if len(bos_.all_magic) == 0:

            bos_.timer.TIMER = 0
            Magic.ATTACK = False

            return 0


class Magic2:
    ATTACK = False
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 5
        self.height = 5

        self.speed = random.uniform(2, 5)

        self.activate = False

        self.is_collised = False

    def use(self):
        if self.activate:
            self.x -= self.speed
    
    @staticmethod
    def foo(bos_, window, player):
        if bos_.timer.TIMER == 1 or Magic.ATTACK:
            Magic.ATTACK = True
            r = 0
            for m in bos_.all_magic:
                m.activate = True
                m.y = r + HEIGHT // 30

                if not m.is_collised:
                    pygame.draw.rect(
                        window, Colors.GREEN,
                        (m.x, m.y, m.width, m.height)
                    )
                    m.use()

                    pl = pygame.Rect(
                        (player.x, player.y),
                        (player.width, player.height)
                    )
                    en = pygame.Rect((m.x, m.y), (m.width, m.height))

                    if not player.teleport_procces:
                        if pl.colliderect(en) == 1:
                            player.XP -= 1
                            player.inj =  True
                            m.is_collised = True

                    if m.x < 0:
                        m.is_collised = True


                r += HEIGHT // 30
        else:
            for m in bos_.all_magic:
                m.x = WIDTH

        num = 0
        for m in bos_.all_magic:
            if m.is_collised:
                num += 1

        if num == len(bos_.all_magic):

            bos_.timer.TIMER = 0
            Magic.ATTACK = False

            return 0


class Magic3:
    ATTACK = False
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 5
        self.height = 5

        self.speed = random.uniform(2, 5)

        self.is_collised = False

        self.activate = False

    def use(self):
        if self.activate:
            self.y += self.speed
    
    @staticmethod
    def foo(bos_, window, player):
        if bos_.timer.TIMER == 1 or Magic.ATTACK:
            Magic.ATTACK = True
            r = 0
            for m in bos_.all_magic:
                m.activate = True
                m.x = r + WIDTH // 35

                if not m.is_collised:
                    pygame.draw.rect(
                        window, Colors.GREEN,
                        (m.x, m.y, m.width, m.height)
                    )
                    m.use()

                    pl = pygame.Rect(
                        (player.x, player.y),
                        (player.width, player.height)
                    )
                    en = pygame.Rect((m.x, m.y), (m.width, m.height))

                    if not player.teleport_procces:
                        if pl.colliderect(en) == 1:
                            player.XP -= 1
                            player.inj =  True
                            m.is_collised = True

                    if m.y > HEIGHT:
                        m.is_collised = True

                r += WIDTH // 35
        else:
            for m in bos_.all_magic:
                m.y = 0

        num = 0
        for m in bos_.all_magic:
            if m.is_collised:
                num += 1

        if num == len(bos_.all_magic):

            bos_.timer.TIMER = 0
            Magic.ATTACK = False

            return 0


class Magic4:
    ATTACK = False
    def __init__(self):
        self.mg = [
            [
                random.randint(0, WIDTH),
                random.randint(0, HEIGHT), 0
            ] for i in range(3)
        ]


    def foo(self, bos_, window, player):
        if bos_.timer.TIMER == 1 or Magic.ATTACK:
            Magic.ATTACK = True

            for num, magic in enumerate(self.mg):
                nn = 0
                if magic[2] <= 500:
                    magic[2] += 1
                for n in range(16):

                    pygame.draw.rect(
                        window, Colors.GREEN,
                        (
                            magic[0] + math.cos(nn) * magic[2],
                            magic[1] + math.sin(nn) * magic[2],
                            5, 5
                        )
                    )


                    pl = pygame.Rect(
                        (player.x, player.y),
                        (player.width, player.height)
                    )
                    en = pygame.Rect(
                        (
                            magic[0] + math.cos(nn) * magic[2],
                            magic[1] + math.sin(nn) * magic[2]
                        ),
                        (5, 5)
                    )

                    if not player.teleport_procces:
                        if pl.colliderect(en) == 1:
                            player.XP -= 1
                            player.inj =  True


                    magic[0] -= 0.1
                    nn += 1


                if (magic[0] + magic[2]) < 0:
                    self.mg.pop(num)

            if len(self.mg) == 0:
                Magic4.ATTACK = False

                return 0


class Magic5:
    ATTACK = False
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 5
        self.height = 5

        self.speed = random.uniform(2, 5)

        self.activate = False

        self.yyy = [i * 150 for i in range(HEIGHT // 100)]

        self.mg = [[Magic(self.x, y_pos) for i in range(20, 50)] for y_pos in self.yyy]

    def use(self, bos_, window, player):
        if bos_.timer.TIMER == 1 or Magic5.ATTACK:
            Magic5.ATTACK = True

            for magic_row in self.mg:
                for num, magic in enumerate(magic_row):
                    magic.x -= magic.speed
                    magic.y += 0.5

                    pygame.draw.rect(
                        window, Colors.GREEN,
                        (magic.x, magic.y, magic.width, magic.height)
                    )

                    pl = pygame.Rect(
                            (player.x, player.y),
                            (player.width, player.height)
                        )
                    en = pygame.Rect((magic.x, magic.y), (magic.width, magic.height))

                    if not player.teleport_procces:
                        if pl.colliderect(en) == 1:
                            player.XP -= 1
                            player.inj =  True
                            magic_row.pop(num)

                    if magic.x < 0:
                        magic_row.pop(num)

        n = 0
        for magic_row in self.mg:
            if len(magic_row) == 0:
                n += 1

        if n == len(self.mg):
            bos_.timer.TIMER = 0
            Magic5.ATTACK = False

            return 0


class Magic6:
    ATTACK = False
    B_X = 0
    B_Y = 0
    X = 1
    Y = 1
    SET = False
    RADIANS = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

        Magic6.B_X = self.x
        Magic6.B_Y = self.y

        self.width = 5
        self.height = 5

        self.speed = 7

    def use(self, bos_, window, player):
        if bos_.timer.TIMER == 1 or Magic6.ATTACK:
            if not Magic6.SET:
                Magic6.X = 2 * player.x - Magic6.B_X
                Magic6.Y = 2 * player.y - Magic6.B_Y
                for i in range(20):
                    if (Magic6.X > 0 and Magic6.X < WIDTH + 20) and (Magic6.Y > 0 and Magic6.Y < HEIGHT + 20):
                        Magic6.X = 2 * Magic6.X - Magic6.B_X
                        Magic6.Y = 2 * Magic6.Y - Magic6.B_Y
                    else:
                        Magic6.RADIANS = math.atan2((self.y - Magic6.Y), (self.x - Magic6.X))
                        break

                Magic6.SET = True

            Magic6.ATTACK = True
            
            dy1 = math.sin(Magic6.RADIANS) * self.speed
            dx1 = math.cos(Magic6.RADIANS) * self.speed
            self.x -= dx1
            self.y -= dy1



            pygame.draw.rect(window, Colors.YELLOW, (self.x, self.y, 5, 5))



            if (self.x < 0 or self.x > WIDTH + 21) or (self.y < 0 or self.y > HEIGHT + 21):
                Magic6.ATTACK = False
                Magic6.SET = False

                bos_.timer.TIMER = 0

                return 0

            pl = pygame.Rect(
                (player.x, player.y),
                (player.width, player.height)
            )
            en = pygame.Rect((self.x, self.y), (self.width, self.height))

            if not player.teleport_procces:
                if pl.colliderect(en) == 1:
                    player.XP -= 1
                    player.inj =  True
                    Magic6.SET = False

                return 0


class Magic7:
    ATTACK = False
    B_X = 0
    B_Y = 0
    X = 1
    Y = 1
    SET = False
    RADIANS = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

        Magic7.B_X = self.x
        Magic7.B_Y = self.y

        self.width = 5
        self.height = 5

        self.speed = 7

        self.mg = [[self.x, self.y, random.uniform(6, 9)] for i in range(10)]

    def use(self, bos_, window, player):
        if bos_.timer.TIMER == 1 or Magic7.ATTACK:
            if not Magic7.SET:
                Magic7.X = 2 * player.x - Magic7.B_X
                Magic7.Y = 2 * player.y - Magic7.B_Y
                for i in range(20):
                    if (Magic7.X > 0 and Magic7.X < WIDTH + 20) and (Magic7.Y > 0 and Magic7.Y < HEIGHT + 20):
                        Magic7.X = 2 * Magic7.X - Magic7.B_X
                        Magic7.Y = 2 * Magic7.Y - Magic7.B_Y
                    else:
                        Magic7.RADIANS = math.atan2((self.y - Magic7.Y), (self.x - Magic7.X))
                        break

                Magic7.SET = True

            Magic7.ATTACK = True


            for num, magic in enumerate(self.mg):
                dy1 = math.sin(Magic7.RADIANS) * magic[2]
                dx1 = math.cos(Magic7.RADIANS) * magic[2]
                magic[0] -= dx1
                magic[1] -= dy1

                pygame.draw.rect(window, Colors.YELLOW, (magic[0], magic[1], 5, 5))

                if (magic[0] < 0 or magic[0] > WIDTH + 21) or (magic[1] < 0 or magic[1] > HEIGHT + 21):
                    self.mg.pop(num)

                pl = pygame.Rect(
                    (player.x, player.y),
                    (player.width, player.height)
                )
                en = pygame.Rect((magic[0], magic[1]), (self.width, self.height))

                if not player.teleport_procces:
                    if pl.colliderect(en) == 1:
                        player.XP -= 1
                        player.inj =  True
                        self.mg.pop(num)
                

                if len(self.mg) == 0:
                    Magic7.ATTACK = False
                    Magic7.SET = False
                    return 0


class Magic8:
    WIDTH = 10
    HEIGHT = 10
    ATTACK = False
    def __init__(self):
        self.x = WIDTH + Magic8.WIDTH
        self.y = HEIGHT // 2 - Magic8.HEIGHT // 2
        self.speed = 1

    def use(self, bos_, window, player):
        if bos_.timer.TIMER == 1 or Magic8.ATTACK:
            self.x -= self.speed
            pygame.draw.rect(window, Colors.RED,
                (
                    (self.x, self.y),
                    (Magic8.WIDTH, Magic8.HEIGHT)
                )
            )
            pygame.draw.circle(
                window,
                (200, 200, 100),
                (
                    math.floor(self.x + Magic8.WIDTH // 2),
                    math.floor(self.y + Magic8.HEIGHT // 2)
                ),
                150, 1
            )

            if not player.teleport_procces:
                if math.sqrt((self.x - player.x) ** 2 + (self.y - player.y) ** 2) < 150:
                    player.XP -= 1
                    player.inj =  True


            if self.x < 0:
                return 0


class MagicManager:
    @staticmethod
    def choise_new_magic(current_magic, bos):
        if current_magic is Magic:
            return [current_magic(bos.x, bos.y) for i in range(random.randint(20, 50))]
        elif current_magic is Magic2:
            return [current_magic(WIDTH + 10, bos.y) for i in range(random.randint(20, 50))]
        elif current_magic is Magic3:
            return [current_magic(bos.x, HEIGHT - 10) for i in range(random.randint(20, 50))]
        elif current_magic is Magic4:
            return current_magic()
        elif current_magic is Magic5:
            return [current_magic(WIDTH + 10, bos.y)]
        elif current_magic is Magic6:
            return current_magic(bos.x, bos.y)
        elif current_magic is Magic7:
            return current_magic(bos.x, bos.y)
        elif current_magic is Magic8:
            return current_magic()



AVAILABLE_MAGIC = [
    Magic, Magic2, Magic3, Magic4,
    Magic5, Magic7, Magic8
]


class FeaturesOfBoss:
    CURRENT_ = 1

    ENEMIES_NOT_SPAWNED = True
    SPAWN_ENEMIES_TIMER = random.randint(2, 4)
    SPAWN_ENEMIES_CURRENT_TIME = 0

    FAST_TELEPORT_FLAG = False
    FAST_TELEPORT_TIMER = random.randint(1, 3)
    FAST_TELEPORT_CURRENT_TIME = 0

    TIMEOUT = True
    HIDDE_TIMEOUT_CURRENT_TIME = 0
    HIDDE_TIMEOUT_TIMER = 3
    HIDDE_TIMER = random.randint(1, 5)
    HIDDE_CURRENT_TIME = 0

    FeaturesLevel = {
        1 : [],
        2 : ["fast_teleport"],
        3 : ["fast_teleport", "hidde"]
    }
    SpawnEnemies = True


    def __init__(self, bos):
        self.abilities_on_level = FeaturesOfBoss.FeaturesLevel.get(bos.number)

    def fast_teleport_(self, bos):
        return True if random.randint(0, 2) == 1 else False

    def hidde_(self, bos):
        return True if random.randint(0, 20) == 1 else False
    
    def chooseAbility(self):
        ...



class Bos(metaclass = BasePropertyMetaClass):
    WIDTH_ = 40
    HEIGHT_ = 50
    def __init__(self, x, y, timer):
        self.number = 1

        self.features = FeaturesOfBoss(self)

        self.x = x
        self.y = y

        self.XP = 1_000

        self.timer = timer

        self.spawn = False

        self.speedX = random.choice((-3, 0, 3))
        self.speedY = random.choice((-3, 0, 3))

        if self.speedX == 0 and self.speedY == 0:
            self.speedX = random.choice((-3, 3))
            self.speedY = random.choice((-3, 3))

        self.current_magic = random.choice(AVAILABLE_MAGIC)
        self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)

        self.K = int(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/waiting.png').get_rect().width * HEIGHT_K)
        self.ANIMATION = [
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/waiting.png'), (self.K, self.K)),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/waiting.png'), (self.K, self.K)),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/waiting.png'), (self.K, self.K)),
            pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/waiting.png'), (self.K, self.K))
        ]

        self.width = self.K // 2
        self.height = self.K // 2

        Bos.WIDTH_ = self.K // 2
        Bos.HEIGHT_ = self.K // 2

        self.headFrame = 1
        self.head = pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/face{self.headFrame}.png'), (self.K + 1, self.K + 1))

        self.inj = False
        self.inj_frame = 1


        self.TELEPORTFRAME = 1
        self.TELEPORTSET = {
            1 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bteleport/1.png'), (37 * int(WIDTH_K), 37 * int(WIDTH_K))),
            2 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bteleport/2.png'), (37 * int(WIDTH_K), 37 * int(WIDTH_K))),
            3 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bteleport/3.png'), (37 * int(WIDTH_K), 37 * int(WIDTH_K))),
            4 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bteleport/4.png'), (37 * int(WIDTH_K), 37 * int(WIDTH_K)))
        }

        self.teleport_procces = False
        self.START = False
        self.ISTELEPORT = False
        self.TIMEFLAGG = False

        self.IS_DIE = False
        self.DIE_FRAME = 1
        self.DIE_IMAGES = {
            1 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/1.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            2 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/2.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            3 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/3.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            4 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/4.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            5 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/5.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            6 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/6.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            7 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/7.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            8 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/8.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            9 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/9.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            10 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/10.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            11 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/11.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K))),
            12 : pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos_die/12.png'), (43 * int(WIDTH_K), 43 * int(WIDTH_K)))
        }

        self.FAST_TELEPORT = False
        self.HIDDE = False

    def fire(self, window, pl):
        if not self.IS_DIE:
            if self.current_magic is Magic:
                if Magic.foo(self, window, pl) == 0:
                    self.current_magic = random.choice(AVAILABLE_MAGIC)
                    self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)

            elif self.current_magic is Magic2:
                if Magic2.foo(self, window, pl) == 0:
                    self.current_magic = random.choice(AVAILABLE_MAGIC)
                    self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)

            elif self.current_magic is Magic3:
                if Magic3.foo(self, window, pl) == 0:
                    self.current_magic = random.choice(AVAILABLE_MAGIC)
                    self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)

            elif self.current_magic is Magic4:
                if self.all_magic.foo(bos_ = self, window = window, player = pl) == 0:
                    self.current_magic = random.choice(AVAILABLE_MAGIC)
                    self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)

            elif self.current_magic is Magic5:
                for m in self.all_magic:
                    if m.use(self, window, pl) == 0:
                        self.current_magic = random.choice(AVAILABLE_MAGIC)
                        self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)

            elif self.current_magic is Magic6:
                if self.all_magic.use(self, window, pl) == 0:
                    self.current_magic = random.choice(AVAILABLE_MAGIC)
                    self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)

            elif self.current_magic is Magic7:
                if self.all_magic.use(self, window, pl) == 0:
                    self.current_magic = random.choice(AVAILABLE_MAGIC)
                    self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)

            elif self.current_magic is Magic8:
                if self.all_magic.use(self, window, pl) == 0:
                    self.current_magic = random.choice(AVAILABLE_MAGIC)
                    self.all_magic = MagicManager.choise_new_magic(self.current_magic, self)
