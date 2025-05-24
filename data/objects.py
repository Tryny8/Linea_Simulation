from core.Linea import Linea

# Définition des objets initiaux

# NOTE: Version CLI
objects_CLI = [
    Linea(10, 10, 1, 1, 1, (255, 0, 0)),
    Linea(25, 20, -1, 1, 25, (0, 255, 0)),
    Linea(50, 10, 1, 1, 1, (0, 255, 0))
]

# NOTE: Version Pygame
objects_Pygame = [
    Linea(100, 2, 1, 10, 1, (255, 0, 0)),
    Linea(300, 1, -1, 10, 3, (0, 255, 0)),
    Linea(500, 0.5, -1, 10, 2, (0, 0, 255)),
    Linea(600, 25, -1, 10, 1, (50, 50, 50))
]

# NOTE: Version Old
# COLORS = [(255, 255, 255), (240, 240, 240)]
# objects = [
#     Linea(x=100, speed=25, direction=1, color=COLORS[0], mass=1),
#     Linea(x=300, speed=1, direction=-1, color=COLORS[1], mass=100)
# ]