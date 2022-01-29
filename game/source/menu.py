from .Config import config
import pygame
import random
import math

Surface_ = pygame.Surface


class Datas:
    WIDTH_K = 0
    HEIGHT_K = 0
    WIDTH = 0

    @classmethod
    def setData(cls_, dataset):
        cls_.WIDTH_K, cls_.HEIGHT_K, cls_.WIDTH = dataset


QUONTITY_OF_BUTTON = 4
BUTTONS_Y = [i * 100 + 300 for i in range(QUONTITY_OF_BUTTON)]

class Button:
    INDEX = 0
    def __init__(self, path):
        self.index = Button.INDEX
        self.path = path
        self.buttonImage = pygame.image.load(path)
        self.width, self.height = (
            round(self.buttonImage.get_rect().width * Datas.WIDTH_K),
            round(self.buttonImage.get_rect().height * Datas.HEIGHT_K)
        )
        self.x, self.y = (
            (Datas.WIDTH // 2) - (self.width // 2) + 30,
            BUTTONS_Y[Button.INDEX]
        )
        self.buttonImage = pygame.transform.scale(
            self.buttonImage,
            (self.width, self.height)
        )
        Button.INDEX += 1

    def setImage(self):
        self.buttonImage = pygame.image.load(self.path)
        self.width, self.height = (
            round(self.buttonImage.get_rect().width * Datas.WIDTH_K),
            round(self.buttonImage.get_rect().height * Datas.HEIGHT_K)
        )
        self.x, self.y = (Datas.WIDTH // 2) - (self.width // 2) + 30, BUTTONS_Y[self.index]
        self.buttonImage = pygame.transform.scale(
            self.buttonImage,
            (self.width, self.height)
        )

    def image(self):
        return self.buttonImage


class Line:
    def __init__(self, xPos, yPos, movement = None):
        self.xPos = xPos
        self.yPos = yPos
        self.movement = movement

        self.max_len_ = random.randint(100, 300)
        self.len_ = 0

        self.is_correct = False
        self.correct_value = 0
        self.stop = False

        self.side = random.choice(("u", "d") if self.movement == "ud" else ("r", "l"))

        self.lineList = [
            [
                (), (), ""
            ],
            [
                (), (), ""
            ]
        ]

        self.speed = random.choice((1, 2))

        self.sx = 0
        self.sy = 0
        if self.side == "l":
            self.sx = config.WIDTH
            self.sy = self.yPos

            self.way = self.sx - random.randint(100, 300)
        elif self.side == "r":
            self.sx = 0
            self.sy = self.yPos

            self.way = self.sx + random.randint(100, 300)
        elif self.side == "u":
            self.sx = self.xPos
            self.sy = config.HEIGHT

            self.way = self.sy - random.randint(100, 300)
        elif self.side == "d":
            self.sx = self.xPos
            self.sy = 0

            self.way = self.sy + random.randint(100, 300)

        self.ex = self.sx
        self.ey = self.sy

    def draw_circle(self, window):
        if not self.is_correct:
            if self.side == "r":
                self.ex += 16
            elif self.side == "l":
                self.ex -= 16
            elif self.side == "u":
                self.ey -= 16
            elif self.side == "d":
                self.ey += 16

            self.is_correct = True

        moveX = 0
        moveY = 0
        if self.side == "r":
            moveX = 16
        elif self.side == "l":
            moveX = -16
        elif self.side == "u":
            moveY = -16
        elif self.side == "d":
            moveY = 16

        pygame.draw.circle(
            window,
            (random.randint(69, 135), 14, 235),
            (
                self.ex + moveX,
                self.ey + moveY
            ), 16, 2
        )

    def draw_line(self, window):
        pygame.draw.line(
            window,
            (random.randint(69, 169), 14, 235),
            (self.sx, self.sy),
            (self.ex, self.ey), 1
        )
        if not self.stop:
            if self.len_ < self.max_len_:
                if self.side == "r":
                    self.ex += self.speed
                    if self.ex == self.way:
                        self.sx = self.ex
                        self.sy = self.ey

                        self.side = random.choice(("u", "d"))
                elif self.side == "d":
                    self.ey += self.speed
                    if self.ey == self.way:
                        self.sx = self.ex
                        self.sy = self.ey

                        self.side = random.choice(("r", "l"))
                elif self.side == "u":
                    self.ey -= self.speed
                    if self.ey == self.way:
                        self.sx = self.ex
                        self.sy = self.ey

                        self.side = random.choice(("r", "l"))
                elif self.side == "l":
                    self.ex -= self.speed
                    if self.ex == self.way:
                        self.sx = self.ex
                        self.sy = self.ey

                        self.side = random.choice(("u", "d"))

                if self.lineList[0][2] == "":
                    self.lineList[0] = [
                        (self.sx, self.sy), (self.ex, self.ey), self.side
                    ]
                else:
                    if self.lineList[0][2] == self.side:
                        self.lineList[0] = [
                            (self.sx, self.sy), (self.ex, self.ey), self.lineList[0][2]
                        ]
                    else:
                        self.lineList[1] = [
                            (self.sx, self.sy), (self.ex, self.ey), self.side
                        ]

                self.len_ += 1
            else:
                self.draw_circle(window)
        else:
            self.draw_circle(window)


class MenuAnimation:
    def __init__(self):
        X_WAY = [(i, 0, "ud") for i in range(0, config.WIDTH, 100)]
        Y_WAY = [(0, i, "rl") for i in range(config.HEIGHT // 7, config.HEIGHT - 100, 100)]
        del X_WAY[0]
        del Y_WAY[0]

        self.lines = [Line(X_WAY[i][0], X_WAY[i][1], X_WAY[i][2]) for i in range(len(X_WAY))]
        self.lines += [Line(Y_WAY[i][0], Y_WAY[i][1], Y_WAY[i][2]) for i in range(len(Y_WAY))]

    def runAnimation(self, window):
        for line in self.lines:

            for l in self.lines:
                if line is not l:
                    for Lineparticle in l.lineList:
                        try:
                            if math.sqrt((line.ex - Lineparticle[1][0]) ** 2 + (line.ey - Lineparticle[1][1]) ** 2) < 100:
                                line.stop = True
                        except:
                            ...

            line.draw_line(window)


class Menu(pygame.Surface):
    MENU = True
    def __init__(self, width, height, fon_path):
        self.animation = MenuAnimation()

        self.width = width
        self.height = height
        self.fon_path = fon_path
        super().__init__((self.width, self.height))

        self.rect = pygame.image.load(fon_path).get_rect()
        self.newX = round(Datas.WIDTH_K * self.rect.width)
        self.newY = round(Datas.WIDTH_K * self.rect.height)

        super().blit(
            pygame.transform.scale(
                pygame.image.load(fon_path).convert_alpha(),
                (
                    self.newX, self.newY
                )
            ).convert_alpha(),
            (0, 0)
        )

        self.buttons = []

        self.cursorImage = self.setCursor()

    def add_button(self, name, path):
        self.buttons.append((name, Button(path)))

    def get_events(self):
        for button in self.buttons:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if (button[1].x <= x <= button[1].x + button[1].width) and (button[1].y <= y <= button[1].y + button[1].height):
                button[1].path = button[1].path.replace("D", "A")
                button[1].setImage()
                return [1, button[0]]
            else:
                if "A" in button[1].path:
                    button[1].path = button[1].path.replace("A", "D")
                    button[1].setImage()
                    return None

        return None

    def show(self, show_animation = True):
        if show_animation:
            self.animation.runAnimation(self)
        for button in self.buttons:
            self.blit(button[1].image(), (button[1].x, button[1].y))

    def setCursor(self):
        self.buttonImage = pygame.image.load("images/menu/cursor/cursor.png").convert_alpha()
        width, height = (
            round(self.buttonImage.get_rect().width * Datas.WIDTH_K),
            round(self.buttonImage.get_rect().height * Datas.HEIGHT_K)
        )
        self.buttonImage = pygame.transform.scale(
            self.buttonImage,
            (width, height)
        ).convert_alpha()

        return [width, height, self.buttonImage]


class MenuSurface(Menu, Surface_):
    def __init__(self, width, height):
        self.animation = MenuAnimation()

        Button.INDEX = 0
        self.width = width
        self.height = height

        Surface_.__init__(self, (self.width, self.height))

        Surface_.fill(self, (0, 0, 0))

        self.buttons = []
        
        self.cursorImage = Menu.setCursor(self)


class SettingsMenu(Menu, Surface_):
    SETTINGS_MENU = False
    def __init__(self, width, height):
        self.animation = MenuAnimation()

        Button.INDEX = 0
        self.width = width
        self.height = height

        Surface_.__init__(self, (self.width, self.height))

        Surface_.fill(self, (0, 0, 0))

        self.buttons = []
        
        self.cursorImage = Menu.setCursor(self)


class LanguageMenu(Menu, Surface_):
    LANGUAGE_MENU = False
    def __init__(self, width, height):
        self.animation = MenuAnimation()

        Button.INDEX = 0

        self.width = width
        self.height = height

        Surface_.__init__(self, (self.width, self.height))

        Surface_.fill(self, (0, 0, 0))

        self.buttons = []
        
        self.cursorImage = Menu.setCursor(self)

class GameMenu(Menu, Surface_):
    GAME_MENU = False
    def __init__(self, width, height):
        self.animation = MenuAnimation()

        Button.INDEX = 0

        self.width = width
        self.height = height

        Surface_.__init__(self, (self.width, self.height))

        Surface_.fill(self, (0, 0, 0))

        self.buttons = []
        
        self.cursorImage = Menu.setCursor(self)