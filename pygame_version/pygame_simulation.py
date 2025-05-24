# Import du projet
import pygame
from pygame_version.renderer import *
import core.physique as physique

# Classe LineaSimulationPygame
class LineaSimulationPygame:
    def __init__(self, width, height, graph_height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Simulation Linea + Graphe position")
        self.clock = pygame.time.Clock()
        self.objects = []
        self.width = width
        self.height = height
        self.graph_height = graph_height
        self.running = True
        self.WHITE = (255, 255, 255)
        self.LIGHT_GRAY = (240, 240, 240)

    def add_object(self, linea):
        self.objects.append(linea)

    def update_physics(self):
        for obj in self.objects:
            physique.move_object(obj, self.width, 1)
            physique.record_position(obj)
        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                physique.handle_collision(self.objects[i], self.objects[j])

    def render(self):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, (0, 0, self.width, self.graph_height))
        for obj in self.objects:
            draw_graph(self.screen, obj, obj.color, self.graph_height - 10, 0.2)
            draw_ball(self.screen, obj)
        pygame.display.flip()

    def run(self, fps):
        while self.running:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update_physics()
            self.render()
        pygame.quit()