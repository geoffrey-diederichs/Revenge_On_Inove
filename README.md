# Revenge_On_Inove

Mini-jeux python en 2D.

## Histoire

Après avoir hacké Inove, un étudiant est punni par son professeur de réseaux : il doit arriver au deuxième étage du bâtiment pour récupérer son ordinateur. Seulement les étudiants et professeurs lui en veulent d'avoir été hacké, il va faloir se battre pour récupérer son ordinateur.

## Mécaniques

Déplacement en 2D dans 3 différentes cartes, collision avec des ennemis positionné au préalable pour ouvrir un mode de combat en tour par tour.

## Détails techniques

### Mécaniques de combats

### character.py

Fichier contenant les classes de personnages utiliser dans le jeux. Les personnages disposent d'items (décrits plus bas), pour calculer les dégats inligés à un autre personnage on additionne l'attaque de l'attaquant, de son item choisie, et soustraie ce total à la défense de la cible. Si le résultat est positif : la cible reçoit les dégats. Si le résultat est nul : il ne se passe rien. Si le résultats est négatif : l'attaquant subit les dégâts. Les personnages disposent d'une liste d'items à laquelle on peut rajouter et enlever des items.

Chaque personnage du jeu dispose de sa classe héritant de la classe Character. La classe Main_character a une variable stockant le niveau du personnage pour lui augmenter ses statistiques en cours de jeu, et la possibilité de réinitialiser ses points de vies après le combat d'un boss (et avant celui du boss final).

### item.py

Fichier contenant les items utilisés par les personnages. Les items sont uniquement caractérisés par un nom et les dégâts qu'ils infligent. 

Chaque item dispose de sa classe héritant de la classe Item et la méthode create() permet de créer des items avec un mot clé non seulement pour que l'on ait pas à manipuler des objets Item depuis le moteur de jeu.

### Pygames

### Cartes
