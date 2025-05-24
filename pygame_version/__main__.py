# Ajout en local
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import du 
from data.objects import objects_Pygame

if __name__ == "__main__":
    # Pour tester indépendamment sans `-m`
    from pygame_simulation import LineaSimulationPygame
else:
    # Pour exécution en tant que module
    from pygame_version.pygame_simulation import LineaSimulationPygame

# Point d'entrée 
# Fenêtre avec espace graphique en haut
WIDTH, HEIGHT = 800, 400
GRAPH_HEIGHT = 200

sim = LineaSimulationPygame(WIDTH, HEIGHT, GRAPH_HEIGHT)
for obj in objects_Pygame:
    sim.add_object(obj)

sim.run(60)