# AC
Automates cellulaires

Ce repo contient des essais sur des automates cellulaires, notamment le *Jeu de la vie* (fichier `gol.py`).

L'affichage de ces automates se fait en utilisant la bilbiothèque curses. La classe `GridPrinter` (voir fichier `grid_printer.py`) permet d'afficher rapidement une grille.
Les grilles sont représentées par des objets `BoolGrid` (voir fichier `bool_grid.py`) pour des grilles contenant uniquement des booléens, ou bien par des objets `Grid` (fichier `grid.py`) pour des grilles plus générales (contenant n'importe quel objet).

