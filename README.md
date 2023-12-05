BEL Alexandre, DIEDERICHS Geoffrey, HANSON Lucas

# Projet Python

Bienvenue dans Revenge On Inove, un jeu d'aventure développé en Python avec Pygame. Dans ce jeu, vous incarnez un étudiant astucieux qui a décidé de hacker son école. Cependant, cette action a rendu tous les étudiants, professeurs, mentors et membres de l'administration furieux contre vous. Pour regagner le contrôle, vous devez vous aventurer dans chaque étage du bâtiment et affronter vos adversaires.

## Instruction

### Objectif
Votre objectif principal est de naviguer à travers les étages de l'école, affronter des adversaires et progresser jusqu'à la victoire finale.

### Contrôles
- Utilisez les touches directionnelles pour vous déplacer dans le bâtiment et interargir avec les menus.
- Appuyez sur la touche d'espace pour courir.
- Utiliser la touche e pour interagir.
- Appuyez sur les chiffres 1-9 pour sélectionner un item ou utiliser l'ascenseur.

### Déroulement du jeu
1. **Début:**
   - Lancer le jeu [en suivant cette démarche](#utilisation).

2. **Exploration des étages:**
   - Parcourez chaque étage du bâtiment et affrontez les ennemis pour progresser.

3. **Affrontements épiques:**
   - Lorsque vous rencontrez un étudiant, un professeur, un mentor ou un membre de l'administration, le jeu bascule en mode combat.
   - Utilisez des tactiques astucieuses pour vaincre vos adversaires et avancer.

4. **Ascenseur:**
   - Terminez tous les combats d'un étage pour débloquer l'ascenseur.
   - Utilisez l'ascenseur pour passer à l'étage suivant.

5. **Répétez le processus:**
   - Répétez l'exploration, les combats et l'utilisation de l'ascenseur jusqu'à ce que vous ayez conquis tous les étages de l'école.

## Utilisation

Tout d'abord vous devez avoir python3. Ensuite pour jouer au jeu, clonez ce projet et allez dans le dossier Code/ :

```bash
$ git clone git@github.com:geoffrey-diederichs/Revenge_On_Inove.git

$ cd Revenge_On_Inove/Code/
```

Vous pouvez installer les modules nécessaires puis exécuter le jeu :

```bash
$ pip install -r requirements.txt

$ python3 main.go
```

Ou bien utiliser un environnement virtuel. Exemple des commandes à exécuter sous Linux :

```bash
$ python3 -m venv env

$ source env/bin/activate

$ pip install -r requirements.txt

$ python3 main.go

$ deactivate
```

## Détails techniques

### I. Mécaniques de combats

#### character.py

Fichier contenant les classes de personnages utiliser dans le jeux. Les personnages disposent d'items (décrits plus bas), pour calculer les dégats inligés à un autre personnage on additionne l'attaque de l'attaquant, de son item choisie, et soustraie ce total à la défense de la cible. Si le résultat est positif : la cible reçoit les dégats. Si le résultat est nul : il ne se passe rien. Si le résultats est négatif : l'attaquant subit les dégâts. Les personnages disposent d'une liste d'items à laquelle on peut rajouter et enlever des items.

Chaque personnage du jeu dispose de sa classe héritant de la classe Character. La classe Main_character a une variable stockant le niveau du personnage pour lui augmenter ses statistiques en cours de jeu, et la possibilité de réinitialiser ses points de vies après le combat d'un boss (et avant celui du boss final).

#### item.py

Fichier contenant les items utilisés par les personnages. Les items sont uniquement caractérisés par un nom et les dégâts qu'ils infligent. 

Chaque item dispose de sa classe héritant de la classe Item et la méthode create() permet de créer des items avec un mot clé pour que l'on ait pas à manipuler des objets Item depuis le moteur de jeu.

### II. Pygames

### III. Cartes

#### floor*.png

Images des maps de chaque étage créées en utilisant l'outil Tiled. Ces cartes permettent à pygame de faire déplacer notre personnage sur l'écran afin de pouvoir explorer. Nous avons une couche cachée par-dessus de chaque image, qui nous permet lorsque nous exportons le fichier, de déterminer si chaque pixel s'agit d'un mur, ou d'un pixel où nous pouvons nous déplacer librement.

#### collisionsMap.py

Fichier contenant des tableaux de valeurs créées lorsque nous exportons la couche collisions des images. Ce fichier nous permet de savoir l'id de chaque pixel dans l'image, et donc de savoir si nous avons le droit de nous déplacer ou pas.

## Axes d'améliorations

### Bug d'affichage sous Windows

Les caractères spéciaux utilisés dans les dialogue etc, s'affichent parfaitement sous Linux mais bug sous Windows.

### Déplacement diagonale

Les déplacement en diagonale (par exemple flèche du haut + flèche gauche) fonctionne parfaitement sous Linux mais pas sous Windows.
