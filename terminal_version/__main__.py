# Ajout en local
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import du projet
from data.objects import objects_CLI

if __name__ == "__main__":
    # Pour tester indépendamment sans `-m`
    from terminal_simulation import LineaSimulationTerminal
else:
    # Pour exécution en tant que module
    from terminal_version.terminal_simulation import LineaSimulationTerminal

# Point d'entrée pour le terminal
sim = LineaSimulationTerminal(sound=True, zoom=1)

for obj in objects_CLI:
    sim.add_object(obj)

sim.run()