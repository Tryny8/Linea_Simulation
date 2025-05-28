# Title

Linea Simulation

# Description

Conception de logiciel Terminal et Pygame avec bibliothèque commune.
Simulateur d'objet sur une ligne (1D) avec gestion de collision (Mur et objets)
Avec ajout d'informations dynamique à propos des objets.

# "Why?" (Motivation/Goal/Problem to solve)

Objectif:
- Créer une ligne ou rebondissent des objets (balles) sans arrêt

Apprentissage et mise en commun des concepts suivants:
- Regroupement de différents codes sur un unique projet 
- Gestion de la physique par bibliothèque
- Gestion d'une idée par deux interface différente (Terminal / Pygame)
- Gestion de la conception logiciel (Contrôleur/Vue/Modèle)
- Architecture de projet professionnel

## Version terminal
![Version terminal](documentation\terminal_version.png)

## Version pygame
![Version pygame](documentation\pygame_version.png)

# Quick Start

```bash
python -m venv venv
source venv/Scripts/activate  # Git Bash ou CMD : venv\Scripts\activate.bat
pip install -r requirements.txt
```

```bash
linea_simulation/
├── data/
│   └── objects.py              # Définition des objets initiaux
├── core/
│   ├── physique.py             # Fonctions physiques communes
│   ├── sound_manager.py        # Gestion centralisée du son
├── terminal_version/
│   ├── __main__.py             # Point d'entrée pour le terminal
│   ├── terminal_simulation.py  # Classe LineaSimulationTerminal
│   └── renderer.py             # TerminalRenderer
├── pygame_version/
│   ├── __main__.py             # Point d'entrée Pygame
│   ├── pygame_simulation.py    # Classe LineaSimulationPygame
│   └── renderer.py             # Renderer Pygame si besoin
├── README.md
├── requirements.txt
└── setup.py                    # (optionnel si installable)
```

# Usage

## Usage avec venv
### Version terminal
```bash
python -m terminal_version
```
### Version Pygame
```bash
python -m pygame_version
```
## Usage sans venv
### Version terminal
```bash
python terminal_version
```
### Version Pygame
```bash
python pygame_version
```

# Contributing
Projet d'apprentissage et recherche d'emploi, pas d'améliorations et de nouvelle options prévu.
Un second projet en 2D puis 3D sont prévu, plus tard.