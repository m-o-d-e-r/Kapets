from sys import flags
from ..Config.config import (
        WIDTH, HEIGHT, RUN,
        FPS, BORDER, WIDTH_K, HEIGHT_K,
        UserEvents, Colors, Timer,
        UserTeleport, show_text, show_fps, AnimationControle
)
from ..capsule import Capsule
from ..bos import FeaturesOfBoss, Bos
from ..player import PlayerAnimation
from ..Config.root_path import BasePath
from ..enemy import Enemy
from ..menu import Menu, SettingsMenu, LanguageMenu, GameMenu
from ..components import Components
import sqlite3
import win32api
import logging
import pygame
import random
import json


class Logger__():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        fh = logging.FileHandler("././datas/logs/data.log")
        formatter = logging.Formatter("[%(asctime)s]:[%(process)d-%(levelname)s]:[%(name)s]:[%(message)s]")

        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def createInfoLog(self, message):
        self.logger.info(message)

    def createErrorLog(self, message):
        self.logger.error(message)

    def createWarningLog(self, message):
        self.logger.warning(message)

class GameVariables:
    CONSTANTS = {}

    @staticmethod
    def add_constant(name, value):
        GameVariables.CONSTANTS.update({name : value})

class GameLoader:
    def __init__(self):
        self.db = sqlite3.connect("././datas/d/main.db")
        self.cursor = self.db.cursor()

        self.jsonResponce = self.readJson()
        self.createTablesResponce = self.createTables(self.jsonResponce)

    def readJson(self):
        with open("././datas/jdata/dStatus.json", "r") as _Jfile:
            JsonData = json.load(_Jfile)

            return JsonData

    def createTables(self, created):
        if not created.get("created"):
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS player(
                x INT,
                y INT);
            """)
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS bos(
                x INT,
                y INT);
            """)
            self.db.commit()

            with open("././datas/jdata/dStatus.json", "w") as _Jfile:
                _Jfile.write(json.dumps({"created" : True}, indent = 4))
            
            Logger__().createInfoLog("Tables created")

            return 0

    def deleteTable(self): ...

    def loadDataBase(self, src = ""): ...

class GameGeneralEvents:
    @staticmethod
    def MainMenuEvents():
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == 3 and event.key == 27)):
                exit()
            menu_event_result = GameVariables.CONSTANTS.get("menu").get_events()

            if menu_event_result is not None:
                if menu_event_result[0] == 1 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if menu_event_result[1] == "exit":
                        pygame.quit()
                        exit()
                    elif menu_event_result[1] == "new_game":
                        MainCycle.PLAYER.XP = 100
                        MainCore.SCENE = "GAME_SURFACE"
                        MainCore.SetEventHandler()
                        Menu.MENU = False
                        SettingsMenu.SETTINGS_MENU = False
                        LanguageMenu.LANGUAGE_MENU = False

                    elif menu_event_result[1] == "settings":
                        MainCore.SCENE = "SETTINGS_MENU"
                        MainCore.SetEventHandler()
                        Menu.MENU = False
                        LanguageMenu.LANGUAGE_MENU = False
                        SettingsMenu.SETTINGS_MENU = True

    @staticmethod
    def SettingsMenuEvents():
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == 3 and event.key == 27)):
                MainCore.SCENE = "MAIN_MENU"
                MainCore.SetEventHandler()
                SettingsMenu.SETTINGS_MENU = False
                LanguageMenu.LANGUAGE_MENU = False
                Menu.MENU = True
            menu_settings_event_result = GameVariables.CONSTANTS.get("settingsMenu").get_events()

            if menu_settings_event_result is not None:
                if menu_settings_event_result[0] == 1 and event.type == 5 and event.button == 1:
                    if menu_settings_event_result[1] == "game":
                        MainCore.SCENE = "GAME"
                        MainCore.SetEventHandler()
                        SettingsMenu.SETTINGS_MENU = False
                        Menu.MENU = False
                        LanguageMenu.LANGUAGE_MENU = False
                        GameMenu.GAME_MENU = True
                    elif menu_settings_event_result[1] == "control":
                        return "control"
                    elif menu_settings_event_result[1] == "language":
                        MainCore.SCENE = "LANGUAGE"
                        MainCore.SetEventHandler()
                        SettingsMenu.SETTINGS_MENU = False
                        Menu.MENU = False
                        LanguageMenu.LANGUAGE_MENU = True

    @staticmethod
    def GameSurfaceEvents(player, window):
        for event in pygame.event.get():
            if player.XP <= 0:
                Components.clear()
                Components.init()

                MainCycle.PLAYER = Components.PLAYER_
                MainCycle.ENEMIS = Components.ENEMIS_
                MainCycle.BOS = Components.BOS_

                MainCore.SCENE = "MAIN_MENU"
                MainCore.SetEventHandler()
                SettingsMenu.SETTINGS_MENU = False
                LanguageMenu.LANGUAGE_MENU = False
                Menu.MENU = True


            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27)):
                Components.clear()
                Components.init()

                MainCycle.PLAYER = Components.PLAYER_
                MainCycle.ENEMIS = Components.ENEMIS_
                MainCycle.BOS = Components.BOS_
                Components.BOS_LIST = (
                    Bos(
                        random.randint(BORDER + 1, WIDTH - BORDER - Bos.WIDTH_ - 1),
                        random.randint(BORDER + 1, HEIGHT - BORDER - Bos.HEIGHT_ - 1), Timer
                        ) for i in range(5)
                )
                MainCore.resetFeaturesOfBoss(True)
                FeaturesOfBoss.ENEMIES_NOT_SPAWNED = True
                FeaturesOfBoss.SPAWN_ENEMIES_TIMER = random.randint(2, 4)
                FeaturesOfBoss.SPAWN_ENEMIES_CURRENT_TIME = 0

                MainCore.SCENE = "MAIN_MENU"
                MainCore.SetEventHandler()
                LanguageMenu.LANGUAGE_MENU = False
                SettingsMenu.SETTINGS_MENU = False
                Menu.MENU = True

            if event.type == pygame.USEREVENT:
                Timer.TIMER = 1
                if FeaturesOfBoss.ENEMIES_NOT_SPAWNED:
                    if FeaturesOfBoss.SPAWN_ENEMIES_CURRENT_TIME == FeaturesOfBoss.FAST_TELEPORT_TIMER:
                        FeaturesOfBoss.ENEMIES_NOT_SPAWNED = False
                    else:
                        FeaturesOfBoss.SPAWN_ENEMIES_CURRENT_TIME += 1

                if MainCycle.BOS.number == 1:
                    if FeaturesOfBoss.FAST_TELEPORT_FLAG:
                        FeaturesOfBoss.FAST_TELEPORT_CURRENT_TIME += 1

                        if FeaturesOfBoss.FAST_TELEPORT_TIMER == FeaturesOfBoss.FAST_TELEPORT_CURRENT_TIME and MainCycle.BOS.XP != 0:
                            MainCycle.BOS.START = True
                            MainCycle.BOS.ISTELEPORT = True
                            MainCycle.BOS.teleport_procces = True

                            FeaturesOfBoss.FAST_TELEPORT_FLAG = False
                            FeaturesOfBoss.FAST_TELEPORT_TIMER = random.randint(1, 3)
                            FeaturesOfBoss.FAST_TELEPORT_CURRENT_TIME = 0

                elif MainCycle.BOS.number == 2:
                    if not FeaturesOfBoss.TIMEOUT:
                        if MainCycle.BOS.HIDDE:
                            FeaturesOfBoss.HIDDE_CURRENT_TIME += 1

                            if FeaturesOfBoss.HIDDE_CURRENT_TIME == FeaturesOfBoss.HIDDE_TIMER and MainCycle.BOS.XP != 0:
                                MainCycle.BOS.HIDDE = False
                                FeaturesOfBoss.HIDDE_CURRENT_TIME = 0
                                FeaturesOfBoss.HIDDE_TIMER = random.randint(1, 5)

                                FeaturesOfBoss.TIMEOUT = True
                    else:
                        FeaturesOfBoss.HIDDE_TIMEOUT_CURRENT_TIME += 1

                        if FeaturesOfBoss.HIDDE_TIMEOUT_TIMER == FeaturesOfBoss.HIDDE_TIMEOUT_CURRENT_TIME:
                            MainCore.resetFeaturesOfBoss(False)
                            FeaturesOfBoss.TIMEOUT = False





            if event.type == UserEvents.TELEPORT_DELAY:
                UserTeleport.TIMEFLAGG = True
                MainCycle.BOS.TIMEFLAGG = True

                if MainCycle.BOS.IS_DIE:
                    MainCycle.BOS.DIE_FRAME += 1

                if MainCycle.CAPSULE.START_TELEPORT_ANIMATION and MainCycle.BOS.IS_DIE:
                    MainCycle.CAPSULE.CURRENT_FRAME = next(MainCycle.CAPSULE.TELEPORT_FRAMES)
                    MainCycle.CAPSULE.TELEPORT_FRAME_NUM += 1

                if MainCycle.CAPSULE.PLAY_ACTIVATION and MainCycle.BOS.IS_DIE:
                    MainCycle.CAPSULE.CURRENT_FRAME = next(MainCycle.CAPSULE.FRAMES)
                    MainCycle.CAPSULE.FRAME_NUM += 1

            if event.type == 5 and event.button == 3 and not UserTeleport.START:
                UserTeleport.X = pygame.mouse.get_pos()[0] - player.width // 2
                UserTeleport.Y = pygame.mouse.get_pos()[1] - player.height // 2

                UserTeleport.START = True
                PlayerAnimation.ISTELEPORT = True
                MainCycle.PLAYER.teleport_procces = True
                


            if event.type == 3 and event.key == 32 and win32api.GetKeyState(1) < 0:
                if not player.shoot_bomb_:
                    player.bomb_.CURSOR_X = pygame.mouse.get_pos()[0]
                    player.bomb_.CURSOR_Y = pygame.mouse.get_pos()[1]
                    player.bomb_.PLAYER_X = player.x
                    player.bomb_.PLAYER_Y = player.y
                    player.bomb_.x = player.x
                    player.bomb_.y = player.y

                    player.shoot_bomb_ = True


            if win32api.GetKeyState(1) < 0 and event.type == UserEvents.SHOOT:
                for num, bullet in enumerate(player.bullets):
                    if not bullet.SHOOT:
                        bullet.X = 0
                        bullet.Y = 0
                        bullet.SET = False
                        bullet.x = player.x
                        bullet.y = player.y
                        bullet.SHOOT = True
                        bullet.CURSOR_X = random.randint(
                                pygame.mouse.get_pos()[0] - 15,
                                pygame.mouse.get_pos()[0] + 15
                            )
                        bullet.CURSOR_Y = random.randint(
                                pygame.mouse.get_pos()[1] - 15,
                                pygame.mouse.get_pos()[1] + 15
                            )
                        bullet.PLAYER_X = player.x
                        bullet.PLAYER_Y = player.y
                        bullet.USER_AIM = 1 if pygame.mouse.get_pos()[0] >= player.x else 0

                        break

            if event.type == UserEvents.BOS_ANIMATION:
                if MainCycle.BOS.headFrame == 4:
                    MainCycle.BOS.headFrame = 1
                else:
                    MainCycle.BOS.headFrame += 1
                MainCycle.BOS.head = pygame.transform.scale(pygame.image.load(f'{BasePath.IMAGES_DIR}/bos/face{MainCycle.BOS.headFrame}.png'), (MainCycle.BOS.K + 1, MainCycle.BOS.K + 1))
                AnimationControle.BOS_K += 1
                if AnimationControle.BOS_K == 4:
                    AnimationControle.BOS_K = 0

                if MainCycle.BOS.inj:    
                    AnimationControle.BOS_INJ_K += 1
                    if AnimationControle.BOS_INJ_K == 2:
                        AnimationControle.BOS_INJ_K = 0

            if event.type == UserEvents.PLAYER_ANIMATION:
                PlayerAnimation.CHANGE_FRAME_FLAG = True

    @staticmethod
    def LanguageEvents():
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == 3 and event.key == 27)):
                MainCore.SCENE = "SETTINGS_MENU"
                MainCore.SetEventHandler()
                Menu.MENU = False
                LanguageMenu.LANGUAGE_MENU = False
                SettingsMenu.SETTINGS_MENU = True

            menu_language_event_result = GameVariables.CONSTANTS.get("languageMenu").get_events()

            if menu_language_event_result is not None:
                if menu_language_event_result[0] == 1 and event.type == 5 and event.button == 1:
                    if menu_language_event_result[1] == "rusian":
                        ...
                    elif menu_language_event_result[1] == "english":
                        ...
    
    @staticmethod
    def ControleEvents(): ...

    @staticmethod
    def GameEvents():
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == 3 and event.key == 27)):
                MainCore.SCENE = "SETTINGS_MENU"
                MainCore.SetEventHandler()
                Menu.MENU = False
                LanguageMenu.LANGUAGE_MENU = False
                GameMenu.GAME_MENU = False
                SettingsMenu.SETTINGS_MENU = True

            menu_game_event_result = GameVariables.CONSTANTS.get("gameMenu").get_events()

            if menu_game_event_result is not None:
                if menu_game_event_result[0] == 1 and event.type == 5 and event.button == 1:
                    if menu_game_event_result[1] == "1":
                        ...
                    elif menu_game_event_result[1] == "2":
                        ...

class MainCore:
    SCENE = "MAIN_MENU"
    MAIN_TREE = {
        "MAIN_MENU" : [
            True,
            {
                "CONTINUE" : [
                    False,
                    GameLoader
                ],
                "NEW_GAME" : [
                    False,
                    ""
                ],
                "SETTINGS_MENU" : [
                    False,
                    {
                        "GAME" : [
                            False,
                            ""
                        ],
                        "CONTROLE" : [
                            False,
                            ""
                        ],
                        "LANGUAGE" : [
                            False,
                            ""
                        ]
                    }
                ]
            }
        ]
    }
    EVENT_CORE = {
        "MAIN_MENU" : GameGeneralEvents.MainMenuEvents,
        "SETTINGS_MENU" : GameGeneralEvents.SettingsMenuEvents,
        "GAME_SURFACE" : GameGeneralEvents.GameSurfaceEvents,
        "LANGUAGE" : GameGeneralEvents.LanguageEvents,
        "CONTROLE" : GameGeneralEvents.ControleEvents,
        "GAME" : GameGeneralEvents.GameEvents
    }
    EVENT_HANDLER = ""
    def __init__(self, window, player, bos, enemis, menu, settingsMenu, languageMenu, gameMenu, clock):
        self.window = window
        self.player = player
        self.bos = bos
        self.enemis = enemis
        self.menu = menu
        self.settingsMenu = settingsMenu
        self.languageMenu = languageMenu
        self.gameMenu = gameMenu
        self.clock = clock

    @staticmethod
    def SetEventHandler():
        MainCore.EVENT_HANDLER = MainCore.EVENT_CORE.get(MainCore.SCENE)

    @staticmethod
    def RunEventHandler():
        return MainCore.EVENT_HANDLER

    def RunGame(self):
        MainCycle(
            self.window, self.player, self.bos, self.enemis,
            self.menu, self.settingsMenu, self.languageMenu, self.gameMenu, self.clock
        ).RunMainCycle()

    def ExtendVariables(self, name, value):
        GameVariables.add_constant(name, value)

    @staticmethod
    def UsertTeleportProcess(window):
        if PlayerAnimation.ISTELEPORT:
            window.blit(
                PlayerAnimation.TELEPORTSET.get(
                    PlayerAnimation.TELEPORTFRAME
                ),
                (
                    MainCycle.PLAYER.x,
                    MainCycle.PLAYER.y
                )
            )

            if UserTeleport.TIMEFLAGG:
                PlayerAnimation.TELEPORTFRAME += 1
                UserTeleport.TIMEFLAGG = False
            if PlayerAnimation.TELEPORTFRAME > 4:
                PlayerAnimation.TELEPORTFRAME = 1

                PlayerAnimation.ISTELEPORT = False
        else:
            MainCycle.PLAYER.x = UserTeleport.X
            MainCycle.PLAYER.y = UserTeleport.Y
            MainCycle.PLAYER.teleport_procces = False

            UserTeleport.START = False

    @staticmethod
    def BosTeleportProcess(window):
        if MainCycle.BOS.ISTELEPORT:
            window.blit(
                MainCycle.BOS.TELEPORTSET.get(
                    MainCycle.BOS.TELEPORTFRAME
                ),
                (
                    MainCycle.BOS.x,
                    MainCycle.BOS.y
                )
            )

            if MainCycle.BOS.TIMEFLAGG:
                MainCycle.BOS.TELEPORTFRAME += 1
                MainCycle.BOS.TIMEFLAGG = False
            if MainCycle.BOS.TELEPORTFRAME > 4:
                MainCycle.BOS.TELEPORTFRAME = 1

                MainCycle.BOS.ISTELEPORT = False
        else:
            MainCycle.BOS.x = random.randint(BORDER + 1, WIDTH - BORDER - MainCycle.BOS.width - 1)
            MainCycle.BOS.y = random.randint(BORDER + 1, HEIGHT - BORDER - MainCycle.BOS.height - 1)

            MainCycle.BOS.speedX = random.choice((-3, 0, 3))
            MainCycle.BOS.speedY = random.choice((-3, 0, 3))

            if MainCycle.BOS.speedX == 0 and MainCycle.BOS.speedY == 0:
                MainCycle.BOS.speedX = random.choice((-3, 3))
                MainCycle.BOS.speedY = random.choice((-3, 3))


            MainCycle.BOS.teleport_procces = False

            MainCycle.BOS.START = False

            MainCycle.BOS.FAST_TELEPORT = False

    @staticmethod
    def enemies_colizion_with_player(pl, enemy, num):
        en = pygame.Rect((enemy.x, enemy.y), (enemy.width, enemy.height))

        if pl.colliderect(en) == 1:
            MainCycle.PLAYER.XP -= 1
            MainCycle.PLAYER.inj = True

            MainCycle.ENEMIS.pop(num)
            MainCycle.ENEMIS.append(
                Enemy(
                    random.randint(BORDER + 1, WIDTH - BORDER - Enemy.WIDTH_ - 1),
                    random.randint(BORDER + 1, HEIGHT - BORDER - Enemy.HEIGHT_ - 1)
                )
            )

    @staticmethod
    def capsule_animation(window):
        if MainCycle.BOS.IS_DIE and MainCycle.CAPSULE.START_TELEPORT_ANIMATION:
            MainCycle.CAPSULE.draw(window)
            if MainCycle.CAPSULE.TELEPORT_FRAME_NUM == 5:
                MainCycle.CAPSULE.START_TELEPORT_ANIMATION = False
                MainCycle.CAPSULE.IS_TELEPORT = False
                MainCycle.CAPSULE.PLAY_ACTIVATION = True
                MainCycle.CAPSULE.IS_ACTIVE = True

        if MainCycle.BOS.IS_DIE and not MainCycle.CAPSULE.START_TELEPORT_ANIMATION:
            if MainCycle.CAPSULE.FRAME_NUM == 12:
                MainCycle.CAPSULE.PLAY_ACTIVATION = False

        if MainCycle.CAPSULE.IS_ACTIVE and not MainCycle.CAPSULE.PLAY_ACTIVATION and MainCycle.BOS.IS_DIE:
            if MainCycle.CAPSULE.collize_with_player(MainCycle.PLAYER) == 1:
                MainCycle.CAPSULE = Capsule()
                MainCycle.COUNT += 1
                MainCycle.BOS = next(Components.BOS_LIST)
                Components.NUM += 1
                MainCycle.BOS.number = Components.NUM

                MainCore.resetFeaturesOfBoss(True)

    @staticmethod
    def activate_player_functions(window):
        MainCycle.PLAYER.spawn = True
        MainCycle.PLAYER.controle(pygame.key.get_pressed(), MainCycle.TICK)
        MainCycle.PLAYER.aim(window, pygame.mouse.get_pos())
        MainCycle.PLAYER.shoot(window, MainCycle.BOS, MainCycle.TICK)
        MainCycle.PLAYER.bomb_activate(window)

    @staticmethod
    def bos_after_dies(window):
        if not MainCycle.BOS.IS_DIE:
            MainCycle.BOS.IS_DIE = True
        else:
            if MainCycle.BOS.DIE_FRAME <= 12:
                window.blit(
                    MainCycle.BOS.DIE_IMAGES.get(MainCycle.BOS.DIE_FRAME),
                    (
                        WIDTH // 2 - MainCycle.BOS.width // 2,
                        HEIGHT // 2 - MainCycle.BOS.height // 2
                    )
                )
            else:
                MainCycle.CAPSULE.IS_TELEPORT = True
                MainCycle.CAPSULE.START_TELEPORT_ANIMATION = True

    @staticmethod
    def resetFeaturesOfBoss(spawn = True):
        if spawn:
            FeaturesOfBoss.ENEMIES_NOT_SPAWNED = True
            FeaturesOfBoss.SPAWN_ENEMIES_TIMER = random.randint(2, 4)
            FeaturesOfBoss.SPAWN_ENEMIES_CURRENT_TIME = 0

        FeaturesOfBoss.FAST_TELEPORT_FLAG = False
        FeaturesOfBoss.FAST_TELEPORT_TIMER = random.randint(5, 10)
        FeaturesOfBoss.FAST_TELEPORT_CURRENT_TIME = 0

        FeaturesOfBoss.TIMEOUT = True
        FeaturesOfBoss.HIDDE_TIMEOUT_CURRENT_TIME = 0
        FeaturesOfBoss.HIDDE_TIMEOUT_TIMER = 3
        FeaturesOfBoss.HIDDE_TIMER = random.randint(1, 5)
        FeaturesOfBoss.HIDDE_CURRENT_TIME = 0

    @staticmethod
    def fast_teleport():
        if not MainCycle.BOS.IS_DIE and MainCycle.BOS.XP != 0:
            if not FeaturesOfBoss.FAST_TELEPORT_FLAG:
                if MainCycle.BOS.features.fast_teleport_(MainCycle.BOS):
                    FeaturesOfBoss.FAST_TELEPORT_FLAG = True
                    MainCycle.BOS.FAST_TELEPORT = True

    @staticmethod
    def hidde():
        if not FeaturesOfBoss.TIMEOUT:
            if not MainCycle.BOS.IS_DIE and not MainCycle.BOS.FAST_TELEPORT and MainCycle.BOS.XP != 0:
                if not MainCycle.BOS.HIDDE:
                    if MainCycle.BOS.features.hidde_(MainCycle.BOS):
                        MainCycle.BOS.HIDDE = True



class MainCycle:
    FIRST = 0
    TICK = 0
    S_TICK = False
    PLAYER = 0
    ENEMIS = 0
    BOS = 0
    CAPSULE = 0
    COUNT = 0
    def __init__(self, window, player, bos, enemis, menu, settingsMenu, languageMenu, gameMenu, clock):
        self.window = window
        MainCycle.PLAYER = player
        MainCycle.BOS = bos
        MainCycle.ENEMIS = enemis
        self.menu = menu
        self.settingsMenu = settingsMenu
        self.languageMenu = languageMenu
        self.gameMenu = gameMenu
        self.clock = clock
        MainCycle.CAPSULE = Capsule()

    def RunMainCycle(self):
        while True:
            self.window.fill((31, 31, 41))

            if MainCycle.S_TICK:
                MainCycle.TICK = (pygame.time.get_ticks() - MainCycle.FIRST) * 0.1
                MainCycle.FIRST = pygame.time.get_ticks()
            else:
                MainCycle.FIRST = pygame.time.get_ticks()
                MainCycle.S_TICK = True


            if MainCore.SCENE == "GAME_SURFACE":
                MainCore.RunEventHandler()(MainCycle.PLAYER, self.window)
            else:
                MainCore.RunEventHandler()()


            if Menu.MENU:
                self.window.blit(self.menu, (0, 0))
                self.menu.show()

                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                self.window.blit(
                    self.menu.cursorImage[2],
                    (
                        x - self.menu.cursorImage[0] // 2,
                        y - self.menu.cursorImage[1] // 2
                    )
                )
            elif SettingsMenu.SETTINGS_MENU:
                self.window.blit(self.settingsMenu, (0, 0))
                self.settingsMenu.show()

                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                self.window.blit(
                    self.settingsMenu.cursorImage[2],
                    (
                        x - self.settingsMenu.cursorImage[0] // 2,
                        y - self.settingsMenu.cursorImage[1] // 2
                    )
                )
            elif LanguageMenu.LANGUAGE_MENU:
                self.window.blit(self.languageMenu, (0, 0))
                self.languageMenu.show()

                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                self.window.blit(
                    self.languageMenu.cursorImage[2],
                    (
                        x - self.languageMenu.cursorImage[0] // 2,
                        y - self.languageMenu.cursorImage[1] // 2
                    )
                )
            elif GameMenu.GAME_MENU:
                self.window.blit(self.gameMenu, (0, 0))
                self.gameMenu.show()

                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                self.window.blit(
                    self.gameMenu.cursorImage[2],
                    (
                        x - self.gameMenu.cursorImage[0] // 2,
                        y - self.gameMenu.cursorImage[1] // 2
                    )
                )

            else:
                if MainCycle.BOS.number == 1:
                    MainCore.fast_teleport()
                elif MainCycle.BOS.number == 2:
                    MainCore.hidde()


                MainCore.activate_player_functions(self.window)

                show_text(self.window, MainCycle.PLAYER.XP, MainCycle.BOS.XP, MainCycle.COUNT)
                show_fps(self.window, self.clock.get_fps())

                for enemy in MainCycle.ENEMIS:
                    if not MainCycle.BOS.IS_DIE:
                        enemy.spawn = True
                    else:
                        enemy.spawn = False





                if MainCycle.PLAYER.XP <= 0:
                    MainCycle.COUNT = 0
                    UserTeleport.COUNT = 5
                    MainCycle.PLAYER.spawn = False

                if MainCycle.BOS.XP <= 0:
                    MainCore.bos_after_dies(self.window)

                MainCore.capsule_animation(self.window)


                if MainCycle.PLAYER.spawn == True:
                    MainCycle.PLAYER.draw(self.window)

                    pl = pygame.Rect(
                        (
                            MainCycle.PLAYER.x,
                            MainCycle.PLAYER.y
                        ),
                        (
                            MainCycle.PLAYER.width,
                            MainCycle.PLAYER.height
                        )
                    )
                    for num, enemy in enumerate(MainCycle.ENEMIS):

#                        if not FeaturesOfBoss.ENEMIES_NOT_SPAWNED:
                        enemy.draw(self.window)

                        if not MainCycle.BOS.IS_DIE:
                            if not MainCycle.PLAYER.teleport_procces:
                                MainCore.enemies_colizion_with_player(pl, enemy, num)


                    MainCycle.BOS.draw(
                        MainCycle.BOS,
                        self.window,
                        (
                            MainCycle.PLAYER.x, MainCycle.PLAYER.y
                        ),
                        MainCycle.TICK
                    )
                    MainCycle.BOS.fire(self.window, MainCycle.PLAYER)



                if UserTeleport.START: # call teleport-method for user
                    MainCore.UsertTeleportProcess(self.window)


                if MainCycle.BOS.START: # call teleport-method for bos after event
                    MainCore.BosTeleportProcess(self.window)




            if GameVariables.CONSTANTS.get("OPENGL_IS_ACTIVE"):
                pygame.display.flip()
            else:
                pygame.display.update()
