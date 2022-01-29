import math
import pygame
import random
from .Config.config import WIDTH, HEIGHT, BORDER, Colors

forward = [1, -1]



class DebugMetaClass(type):
    def __new__(cls_, name, parents, attr):

        #attr.pop("movement_1")
        #attr.pop("movement_2")
        #attr.pop("movement_3")
        #attr.pop("movement_4")
        #attr.pop("movement_5")
        #attr.pop("movement_6")
        attr.pop("movement_7")


        return type(name, parents, attr)



class Movement(metaclass = DebugMetaClass):
    def __init__(self) -> None:
        self.TYPES = {
            "movement_1" : self.movement_1,
            "movement_2" : self.movement_2,
            "movement_3" : self.movement_3,
            "movement_4" : self.movement_4,
            "movement_5" : self.movement_5,
            "movement_6" : self.movement_6,
            #"movement_7" : self.movement_7
        }

    def movement_1(self, x, y, speed, offset):
        x += speed
        y = x ** 0.5 + offset

        return x, y

    def movement_2(self, x, y, speed, offset):
        y += speed
        x = y ** 0.5 + offset

        return x, y

    def movement_3(self, x, y, speedX, speedY):
        x += speedX
        y += speedY

        return x, y

    def movement_4(self, x, y, speedX):
        x += speedX

        return x, y

    def movement_5(self, x, y, speedY):
        y += speedY

        return x, y

    def movement_6(self, x, y, speedX, offset):
        x += speedX

        y = x // 4 + offset

        return x, y

    def movement_7(self, x, y, speedX):
        t = 10 // math.pi

        x = math.cos(t)
        y = math.sin(t)

        return x, y



class Enemy:
    WIDTH_ = 10
    HEIGHT_ = 10
    def __init__(self, x, y):
        self.speed = random.randint(1, 5)

        self.spawn = False

        self.offset = random.randint(0, HEIGHT - 50)

        self.x = x
        self.y = y
        self.width = 10
        self.height = 10

        self.speedX = self.speed * random.choice(forward)
        self.speedY = self.speed * random.choice(forward)

        self.datas_move = []
        self.type_of_movement = ""
        self.number_movement = 0
        while True:
            self.type_of_movement = random.choice(dir(Movement))
            if self.type_of_movement.startswith("movement_"):
                if "1" in self.type_of_movement:
                    self.datas_move = [self.x, self.y, self.speedX, self.offset]
                    self.number_movement = 1
                elif "2" in self.type_of_movement:
                    self.number_movement = 2
                    self.datas_move = [self.x, self.y, self.speedY, self.offset]
                elif "3" in self.type_of_movement:
                    self.number_movement = 3
                    self.datas_move = [self.x, self.y, self.speedX, self.speedY]
                elif "4" in self.type_of_movement:
                    self.number_movement = 4
                    self.datas_move = [self.x, self.y, self.speedX]
                elif "5" in self.type_of_movement:
                    self.number_movement = 5
                    self.datas_move = [self.x, self.y, self.speedY]
                elif "6" in self.type_of_movement:
                    self.number_movement = 6
                    self.datas_move = [self.x, self.y, self.speedX, self.offset]
                elif "7" in self.type_of_movement:
                    self.number_movement = 7
                    self.datas_move = [self.x, self.y, self.speedX]


                self.type_of_movement = Movement().TYPES.get(self.type_of_movement)

                break

    def update_datas_move(self, ) -> list:
        if self.number_movement == 1:
            return [self.x, self.y, self.speedX, self.offset]

        if self.number_movement == 2:
            return [self.x, self.y, self.speedY, self.offset]

        if self.number_movement == 3:
            return [self.x, self.y, self.speedX, self.speedY]

        if self.number_movement == 4:
            return [self.x, self.y, self.speedX]

        if self.number_movement == 5:
            return [self.x, self.y, self.speedY]

        if self.number_movement == 6:
            return [self.x, self.y, self.speedX, self.offset]

        if self.number_movement == 7:
            return [self.x, self.y, self.speedX]

    def draw(self, window):
        if self.spawn:
            self.x, self.y = self.type_of_movement(*self.datas_move)


            if self.x <= BORDER:
                self.speedX = -self.speedX
            if self.y <= BORDER:
                self.speedY = -self.speedY

            if self.x >= WIDTH - BORDER:
                self.speedX = -self.speedX
            if self.y >= HEIGHT - BORDER:
                self.speedY = -self.speedY


            pygame.draw.rect(window, Colors.RED, (self.x, self.y, self.width, self.height))

            self.datas_move = self.update_datas_move()