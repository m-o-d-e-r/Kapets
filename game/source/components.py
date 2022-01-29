from .Config.config import (
    BORDER, WIDTH, HEIGHT, Timer
)
from .player import Player
from .enemy import Enemy
from .bos import Bos
import random


class Components:
    PLAYER_ = None
    ENEMIS_ = []
    BOS_ = None
    BOS_LIST = []
    NUM = 1

    @staticmethod
    def init():
        Components.PLAYER_ = Player()
        for i in range(20):
            Components.ENEMIS_.append(
                Enemy(
                    random.randint(BORDER + 1, WIDTH - BORDER - Enemy.WIDTH_ - 1),
                    random.randint(BORDER + 1, HEIGHT - BORDER - Enemy.HEIGHT_ - 1)
                )
            )
        Components.BOS_ = Bos(
            random.randint(BORDER + 1, WIDTH - BORDER - Bos.WIDTH_ - 1),
            random.randint(BORDER + 1, HEIGHT - BORDER - Bos.HEIGHT_ - 1), Timer
            )

        Components.BOS_LIST = (
            Bos(
                random.randint(BORDER + 1, WIDTH - BORDER - Bos.WIDTH_ - 1),
                random.randint(BORDER + 1, HEIGHT - BORDER - Bos.HEIGHT_ - 1), Timer
                ) for i in range(5)
        )

    @staticmethod
    def clear():
        Components.PLAYER_ = None
        Components.ENEMIS_ = []
        Components.BOS_ = None