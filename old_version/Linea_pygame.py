import pygame
import sys

# Initialisation Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation Linea - Pygame")

# Couleurs
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 100, 100)

# Horloge
CLOCK = pygame.time.Clock()
FPS = 60

class Linea:
    quantity = 0
    def __init__(self, x, speed, direction, radius=10):
        self.id = Linea.quantity
        Linea.quantity += 1
        self.x = x
        self.y = HEIGHT // 2
        self.speed = speed
        self.direction = direction
        self.radius = radius
        self.color = BLUE

    def move(self):
        self.x += self.speed * self.direction

    def bounce_edges(self):
        if self.x + self.radius >= WIDTH:
            self.direction = -1
        elif self.x - self.radius <= 0:
            self.direction = 1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), self.y), self.radius)

    def check_collision(self, other):
        distance = abs(self.x - other.x)
        if distance < self.radius * 2:
            # Simple échange de directions
            self.direction *= -1
            other.direction *= -1
            self.color = RED
            other.color = RED
        else:
            self.color = BLUE
            other.color = BLUE

# Création des objets
objects = [
    Linea(x=100, speed=3, direction=1),
    Linea(x=300, speed=2, direction=-1),
    Linea(x=500, speed=4, direction=1)
]

# Boucle principale
running = True
while running:
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mettre à jour la position
    for obj in objects:
        obj.move()
        obj.bounce_edges()

    # Détection de collisions
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            objects[i].check_collision(objects[j])

    # Dessin
    for obj in objects:
        obj.draw(SCREEN)

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
sys.exit()
