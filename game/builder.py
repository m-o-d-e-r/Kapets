from cx_Freeze import setup, Executable
import sys

class Builder:
    NAME = "Game"
    VERSION = "0.0.1"
    DESCRIPTION = ""
    EXECUTABLES = [
        Executable('main.py', targetName = 'main.exe'),
        Executable('source/player.py', targetName = 'source/player.exe'),
        Executable('source/bos.py', targetName = 'source/bos.exe'),
        Executable('source/enemy.py', targetName = 'source/enemy.exe'),
        Executable('source/menu.py', targetName = 'source/menu.exe'),
        Executable('source/components.py', targetName = 'source/components.exe'),
        Executable('source/Config/config.py', targetName = 'source/Config/config.exe'),
        Executable('source/Config/root_path.py', targetName = 'source/Config/root_path.exe'),
    ]
    _EXCLUDE = [
        'logging', 'email', 'html', 'http', 'urllib',
        'xml', 'pydoc', 'doctest', 'argparse', 'datetime', 'zipfile',
        'subprocess', 'pickle', 'threading', 'locale', 'calendar',
        'tokenize', 'base64', 'gettext',
        'bz2', 'fnmatch', 'getopt', 'string', 'stringprep',
        'quopri', 'copy', 'imp', 'linecache',
        'asyncio', 'OpenGL', 'PyQt5'
    ]
    _INCLUDE = ['tkinter', 'pygame', 'numpy', 'fnmatch', 'ctypes']
    OPTIONS = {
        'build_exe': {
            'include_msvcr': True,
           'excludes': _EXCLUDE,
            'zip_include_packages': _INCLUDE,
            'build_exe': 'build',
        }
    }

    @staticmethod
    def build():
        setup(
            name = Builder.NAME,
            version = Builder.VERSION,
            description = Builder.DESCRIPTION,
            executables = Builder.EXECUTABLES,
            options = Builder.OPTIONS
        )

def help():
    print(
        """
            python builder.py set name={} version={} description={} include={} exclude={}
            python builder.py show
            python builder.py build
        """
    )

def ckeck_argv(args):
    print(args)

if __name__ == "__main__":
    ckeck_argv(sys.argv[1 : len(sys.argv)])
#    Builder.build()


#http://bloktetradi.com.ua/?utm_source=google&utm_medium=cpc&utm_campaign=bloktetradi&utm_term=keywords&gclid=EAIaIQobChMIg-Dhw6mS8gIVh94YCh0AFgUuEAAYASAAEgKjQ_D_BwE
