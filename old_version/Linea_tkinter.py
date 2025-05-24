import tkinter as tk
import time

class Linea:
    quantity = 0
    def __init__(self, canvas, x, vitesse, direction, radius=10):
        self.canvas = canvas
        self.id = Linea.quantity
        Linea.quantity += 1
        self.x = x
        self.vitesse = vitesse
        self.direction = direction
        self.radius = radius
        self.y = 100  # Position verticale fixe pour animation 1D
        self.oval = self.canvas.create_oval(self.x - radius, self.y - radius,
                                            self.x + radius, self.y + radius,
                                            fill="blue")

    def move(self):
        dx = self.vitesse * self.direction
        self.x += dx
        self.canvas.move(self.oval, dx, 0)

    def bounce_if_needed(self, left, right):
        if self.x + self.radius >= right:
            self.direction = -1
        elif self.x - self.radius <= left:
            self.direction = 1

    def check_collision(self, other):
        if abs(self.x - other.x) < self.radius * 2:
            self.direction *= -1
            other.direction *= -1

class MapLinea:
    def __init__(self, root, width=500, height=200):
        self.canvas = tk.Canvas(root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.width = width
        self.height = height
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def animate(self):
        for obj in self.objects:
            obj.move()
            obj.bounce_if_needed(0, self.width)
        
        # Vérifie les collisions entre objets
        for i in range(len(self.objects)):
            for j in range(i+1, len(self.objects)):
                self.objects[i].check_collision(self.objects[j])

        # Rafraîchir la fenêtre
        root.after(30, self.animate)

# ---- Lancement ----
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulation Linea")

    map_linea = MapLinea(root)
    map_linea.add_object(Linea(map_linea.canvas, x=50, vitesse=5, direction=1))
    map_linea.add_object(Linea(map_linea.canvas, x=200, vitesse=5, direction=-1))
    map_linea.add_object(Linea(map_linea.canvas, x=300, vitesse=5, direction=1))

    map_linea.animate()
    root.mainloop()
