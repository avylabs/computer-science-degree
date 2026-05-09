from cx_Freeze import setup, Executable

buildOptions = dict(include_files = ['./assets/'])

setup(
    name="Pysteroids",
    version="1.0",
    description="Um clone de Asteroids feito em Python com o Pygame-CE",
    author = "Aveline Cacciatore",
    options = dict(build_exe = buildOptions),
    executables=[Executable("main.py")]
)