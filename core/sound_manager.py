from threading import Thread
from winsound import Beep
from queue import Queue

# Gestion centralisée du son
class SoundManager:
    def __init__(self):
        self.queue = Queue()
        self.thread = Thread(target=self._sound_loop, daemon=True)
        self.thread.start()

    def _sound_loop(self):
        while True:
            freq, dur = self.queue.get()
            try:
                Beep(freq, dur)
            except RuntimeError:
                pass  # Gère le cas rare où le son échoue
            self.queue.task_done()

    def play(self, freq, dur):
        self.queue.put((freq, dur))