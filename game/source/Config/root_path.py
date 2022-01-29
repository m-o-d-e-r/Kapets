import os
import sys


class BasePath:
    __BASE_DIR__ = os.path.dirname(os.path.abspath("main.py"))
    IMAGES_DIR = __BASE_DIR__ + "\images\\"
    SOURCE_DIR = __BASE_DIR__ + "\source\\"

    def __str__(self):
        return f"""
                [+] BASE_DIR\t{BasePath.__BASE_DIR__}
                [+] IMAGES_DIR\t{BasePath.IMAGES_DIR}
                [+] SOURCE_DIR\t{BasePath.SOURCE_DIR}
                """
