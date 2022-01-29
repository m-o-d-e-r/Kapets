from source.Config.config import (
    WIDTH, HEIGHT,
    WIDTH_K, HEIGHT_K
)
import pygame


class Capsule:
    def __init__(self):
        self.TIMEOUT = 0

        self.WK, self.HK = (15 * int(WIDTH_K), 26 * int(WIDTH_K))


        self.IS_COLLISED = False
        self.IS_ACTIVE = False

        self.IS_TELEPORT = False
        self.START_TELEPORT_ANIMATION = False
        self.TELEPORT_FRAMES = (pygame.transform.scale(pygame.image.load(f"images/capsule/show/{i}.png"), (15 * int(WIDTH_K), 13 * int(WIDTH_K))) for i in range(6))
        self.TELEPORT_FRAME_NUM = 0

        self.PLAY_ACTIVATION = False
        self.FRAMES = (pygame.transform.scale(pygame.image.load(f"images/capsule/activation/{i}.png"), (self.WK, self.HK)) for i in range(12))
        self.CURRENT_FRAME = next(self.TELEPORT_FRAMES)
        self.FRAME_NUM = 0

        self.x = WIDTH // 2 - self.WK // 2
        self.y = HEIGHT // 2 - self.HK // 2

    def draw(self, window):
        window.blit(
            self.CURRENT_FRAME,
            (
                self.x,
                self.y
            )
        )

    def collize_with_player(self, player):
        player_rect = pygame.Rect(
            (
                player.x, player.y
            ),
            (
                player.width, player.height
            )
        )

        capsule_rect = pygame.Rect(
            (
                self.x, self.y
            ),
            (
                self.WK, self.HK
            )
        )

        if player_rect.colliderect(capsule_rect) == 1:
            return 1
