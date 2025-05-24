# Import du projet
from keyboard import is_pressed
from time import time, sleep
from shutil import get_terminal_size

from terminal_version.renderer import TerminalRenderer

import core.physique as physique
from core.fps_counter import FPSCounter
from core.sound_manager import SoundManager

# Classe LineaSimulationTerminal
class LineaSimulationTerminal:
    def __init__(self, sound=True, zoom=2.0):
        self.sound = sound
        self.key_code = "q"
        self.sound_manager = SoundManager()
        self.beep(tone='default', duration=400)
        columns, _ = get_terminal_size()
        self.width = columns - 2  # pour éviter d'aller trop à droite
        self.zoom = zoom  # facteur d'agrandissement pour affichage
        self.physical_width = self.width / zoom
        self.edge_left = 0
        self.edge_right = self.physical_width
        self.objects = []
        self.collision_count = 0
        self.running = True
        self.time_step = 0
        self.frame = 0
        self.fps_counter = FPSCounter()
        self.renderer = TerminalRenderer(n_lines=4)

    def add_object(self, linea):
        self.objects.append(linea)

    def move_object_terminal(self, obj, dt):
        obj.x += obj.speed * obj.direction * dt

        # Rebond personnalisé avec bip
        if obj.x - obj.radius <= 0:
            obj.x = obj.radius
            obj.direction *= -1
            self.collision_count += 1
            self.beep(tone='wall', duration=25)
        elif obj.x + obj.radius >= self.physical_width:
            obj.x = self.physical_width - obj.radius
            obj.direction *= -1
            self.collision_count += 1
            self.beep(tone='wall', duration=25)

    def update_physics(self, dt):
        for obj in self.objects:
            self.move_object_terminal(obj, dt)
            physique.record_position(obj)

        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                if physique.are_colliding(self.objects[i], self.objects[j]):
                    physique.handle_collision(self.objects[i], self.objects[j])
                    self.collision_count += 1
                    self.beep(tone='collision', duration=25) # Collision détectée → bip

    def build_display_lines(self):
        # Échelle visuelle
        scale = ''.join(
        '+' if i % 10 == 0 else '|' if i % 5 == 0 else ' ' for i in range(self.width)
        )
        # Ligne vide
        display = ['_' for _ in range(self.width)]

        # Affichage des objets
        for obj in self.objects:
            pos = int((obj.x - self.edge_left) * self.zoom)
            if 0 <= pos < self.width:
                if display[pos] == '_':
                    display[pos] = 'O'
                else:
                    display[pos] = 'X'  # collision visuelle

        display[0] = '|'
        display[-1] = '|'
        
        velocities = " | ".join([f"v{i+1}={obj.speed:.2f}" for i, obj in enumerate(self.objects)])
        masses = " | ".join([f"v{i+1}={obj.mass:.2f}" for i, obj in enumerate(self.objects)])
        
        # Affichage terminal
        status = (f"[Step: {self.time_step}]"
                    f"[Objects: {len(self.objects)}]"
                    f"[Zoom: x{self.zoom:.1f}]"
                    f"[Width: {self.width}]"
                    f"[Collisions: {self.collision_count}]"
                    f"[FPS: {self.fps_counter.get_fps()}]"
                    f"[{velocities}]"
                    f"[{masses}]")
        self.time_step += 1

        return [scale, "".join(display), status]

    def beep(self, tone, duration):
        if self.sound != True:
            return
        
        if tone == 'wall':
            frequence = 2500   # Bord : son aigu
        elif tone == 'collision':
            frequence = 440  # Collision : son grave
        else:
            frequence = 1000   # Par default
        
        print(f"[BEEP:{tone}]", end=' ', flush=True)
        self.sound_manager.play(frequence, duration)

    def render(self):
        lines = self.build_display_lines()
        self.renderer.render(lines)

    def run(self, dt=0.008, display_delay=0.0163):
        last_time = time()
        accumulator = 0.0
        
        try:
            while self.running:                
                now = time()
                frame_time = now - last_time
                last_time = now
                accumulator += frame_time
                
                if is_pressed(self.key_code):
                    print(f"[Touche Pressed: {self.key_code} - Simulation arrêtée]")
                    break
                
                while accumulator >= dt:
                    self.update_physics(dt)
                    accumulator -= dt
                
                self.render()
                self.fps_counter.tick()  # Mise à jour du compteur FPS
                
                sleep(display_delay)
                self.frame += 1
        
        except KeyboardInterrupt:
            print("\nSimulation arrêtée par l'utilisateur.")