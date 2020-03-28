import random
import matplotlib.pyplot as plt

class Maillon:

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

class Pile:

    def __init__(self):
        self.taille = 0
        self.sommet = None

    def empiler(self, valeur):
        self.sommet = Maillon(valeur, self.sommet)
        self.taille += 1

    def depiler(self):
        if self.taille > 0:
            valeur = self.sommet.valeur
            self.sommet = self.sommet.suivant
            self.taille -= 1
            return valeur

    def est_vide(self):
        return self.taille == 0

    def lire_sommet(self):
        return self.sommet.valeur

# Dimensions de la grille
LARGEUR = 40
HAUTEUR = 30

def voisinage(couple):
    """
        Renvoi la liste des cellules voisines 
        de la cellule (ligne, colonne) = couple dans la grille
    """
    liste_voisins = []
    i, j = couple[0], couple[1]
    for d in (-1, 1):
        if -1 < i+d < HAUTEUR:
            liste_voisins.append((i+d, j))
        if -1 < j+d < LARGEUR:
            liste_voisins.append((i, j+d))
    
    return liste_voisins

def dfs(s):
    P = {s: None}
    Q = Pile()
    Q.empiler(s)

    while not (Q.est_vide()):
        u = Q.lire_sommet()
        R = [y for y in voisinage(u) if y not in P]

        if R:
            v = random.choice(R)
            P[v] = u
            Q.empiler(v)
        else:
            Q.depiler()

    return P

def dedale():
    """
        Fonction dessinant le resultat.
    """
    labyrinthe = [[0 for j in range(2*LARGEUR+1)] for i in range(2*HAUTEUR+1)]
    parcours = dfs((0, 0))

    for i, j in parcours:
        labyrinthe[2*i+1][2*j+1] = 1
        if (i, j) != (0,0):
            k, l = parcours[(i, j)]
            labyrinthe[2*k+1][2*l+1] = 1
            labyrinthe[i+k+1][j+l+1] = 1

    labyrinthe[1][0] = 1
    labyrinthe[2*HAUTEUR-1][2*LARGEUR] = 1

    # Graphique
    plt.imshow(labyrinthe)
    # On cache les graduations
    plt.xticks([])
    plt.yticks([])
    # On visualise le resultat
    plt.show()

dedale()