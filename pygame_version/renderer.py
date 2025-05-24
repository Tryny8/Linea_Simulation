# Renderer Pygame si besoin

def draw_graph(screen, obj, color, offset_y, scale):
    import pygame
    if len(obj.positions) > 1:
        for i in range(1, len(obj.positions)):
            pygame.draw.line(screen, color,
                             (50 + i - 1, offset_y - obj.positions[i - 1] * scale),
                             (50 + i, offset_y - obj.positions[i] * scale), 2)

def draw_ball(screen, obj):
    import pygame
    pygame.draw.circle(screen, obj.color, (int(obj.x), int(obj.y)), obj.radius)