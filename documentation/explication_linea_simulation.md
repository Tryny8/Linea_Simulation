
# Décomposition de la classe `LineaSimulation`

La classe `LineaSimulation` encapsule toute la logique de la simulation Pygame (animation et graphique de trajectoire). Elle est conçue pour organiser proprement les composants physiques, visuels, et la boucle d'exécution.

---

## 🧱 Structure générale de la classe

```python
class LineaSimulation:
```
> C’est le **coeur de ton programme**. Elle orchestre tout : création de la fenêtre, gestion des objets, rendu et logique physique.

---

## 1. `__init__()` : Initialisation

```python
def __init__(self, width, height, graph_height):
```
Prépare tout ce dont la simulation a besoin :

| Élément             | Rôle |
|---------------------|------|
| `pygame.init()`     | Démarre le moteur graphique Pygame |
| `self.screen`       | Surface principale de la fenêtre |
| `self.clock`        | Permet de contrôler le **framerate** |
| `self.objects`      | Liste des objets de type `Linea` |
| `self.width`/`height` | Dimensions de la fenêtre |
| `self.graph_height` | Hauteur du graphe position/temps |
| `self.running`      | Contrôle de la boucle de simulation |

**🎯 But** : centraliser la configuration de départ de manière claire.

---

## 2. `add_object()` : Ajout dynamique d’objet

```python
def add_object(self, linea):
    self.objects.append(linea)
```

Permet d'ajouter dynamiquement des objets. Utile pour une interface ou le chargement depuis un fichier.

---

## 3. `update_physics()` : Mise à jour de la logique physique

```python
def update_physics(self):
    for obj in self.objects:
        move_object(obj, self.width)
        record_position(obj)
    for i in range(len(self.objects)):
        for j in range(i + 1, len(self.objects)):
            handle_collision(self.objects[i], self.objects[j])
```

- Gère les déplacements et enregistre les positions
- Vérifie les collisions entre objets

**🎯 But** : séparer la logique de la simulation de l'affichage.

---

## 4. `render()` : Affichage

```python
def render(self):
    self.screen.fill(WHITE)
    # fond du graphe
    # tracés des courbes
    # dessins des boules
    pygame.display.flip()
```

- Vide l'écran
- Dessine la zone du graphe et chaque objet
- Met à jour l'affichage

**🎯 But** : gérer tout le rendu en un seul endroit.

---

## 5. `run(fps)` : Boucle principale

```python
def run(self, fps):
    while self.running:
        self.clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.update_physics()
        self.render()
```

Gère la boucle classique d'une simulation temps réel :
1. Lecture des événements utilisateur
2. Mise à jour logique
3. Affichage

---

## 🧠 Pourquoi ce découpage ?

- **Modularité** : changement d'un composant sans affecter les autres
- **Lisibilité** : logique bien structurée et séparée
- **Évolutivité** : facile d’ajouter de nouveaux comportements
- **Testabilité** : chaque fonction est autonome

---

Souhaits possibles :
- Ajouter un système d'ajout d'objets interactif
- Export des données
- Interface plus poussée
