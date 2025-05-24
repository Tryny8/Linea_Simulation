from core.color_manager import get_color_name

# Classe Linea
class Linea:
    def __init__(self, x, speed, direction, radius, mass, color):
        self.x = x
        self.speed = speed
        self.direction = direction
        self.mass = mass
        self.color = color
        self.radius = radius
        self.positions = []
        self.y = 200 + 100
    
    def __repr__(self):
        return f"Obj {get_color_name(self.color)}: {self.speed}"