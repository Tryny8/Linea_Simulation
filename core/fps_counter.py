from time import time

class FPSCounter:
    def __init__(self):
        self.last_time = time()
        self.frame_counter = 0
        self.fps = 0

    def tick(self):
        """Appelée à chaque frame pour compter."""
        self.frame_counter += 1
        now = time()
        elapsed = now - self.last_time

        if elapsed >= 1.0:
            self.fps = self.frame_counter
            self.frame_counter = 0
            self.last_time = now

    def get_fps(self):
        """Retourne le FPS actuel."""
        return self.fps