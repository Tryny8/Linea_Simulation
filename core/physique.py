# Fonctions physiques communes

def move_object(obj, map_width, dt):
    # NOTE: le dt n'est pas necessaire dans Pygame
    obj.x += obj.speed * obj.direction * dt
    bounce_on_edges(obj, map_width)

def bounce_on_edges(obj, map_width):
    if obj.x - obj.radius <= 0:
        obj.x = obj.radius
        obj.direction *= -1
    elif obj.x + obj.radius >= map_width:
        obj.x = map_width - obj.radius
        obj.direction *= -1

def record_position(obj, max_points=500):
    obj.positions.append(obj.x)
    if len(obj.positions) > max_points:
        obj.positions.pop(0)


def handle_collision(obj1, obj2):
    if are_colliding(obj1, obj2):
        apply_elastic_collision(obj1, obj2)
        separate_objects(obj1, obj2)

def are_colliding(obj1, obj2):
    # if abs(obj1.x - obj2.x) < (obj1.radius + obj2.radius):
    #     print("Colision!!!", obj1, obj2)
    return abs(obj1.x - obj2.x) < (obj1.radius + obj2.radius)

def apply_elastic_collision(a, b):
    v1, v2 = a.speed * a.direction, b.speed * b.direction
    m1, m2 = a.mass, b.mass

    new_v1 = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
    new_v2 = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)

    a.direction = 1 if new_v1 > 0 else -1
    b.direction = 1 if new_v2 > 0 else -1
    a.speed = abs(new_v1)
    b.speed = abs(new_v2)

def separate_objects(a, b):
    distance = abs(a.x - b.x)
    overlap = (a.radius + b.radius) - distance
    shift = overlap / 2 + 0.1
    if a.x < b.x:
        a.x -= shift
        b.x += shift
    else:
        a.x += shift
        b.x -= shift
