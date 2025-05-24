from sys import stdout

# Classe TerminalRenderer
class TerminalRenderer:
    def __init__(self, n_lines):
        self.n_lines = n_lines
        self.first_frame = True

    def render(self, lines):
        if not self.first_frame:
            # Revenir en haut de l'affichage précédent
            for _ in range(self.n_lines):
                stdout.write("\033[F")  # curseur ligne précédente
                stdout.write("\033[2K")  # efface ligne entière
        else:
            self.first_frame = False

        for line in lines:
            print(line)

        stdout.flush()