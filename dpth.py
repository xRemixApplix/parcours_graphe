# Modules
import random

# Modelisation du graphe
Graph = dict()
Graph['a'] = ['b','c']
Graph['b'] = ['a','d','e']
Graph['c'] = ['a','d']
Graph['d'] = ['b','c','e']
Graph['e'] = ['b','d','f','g']
Graph['f'] = ['e','g']
Graph['g'] = ['e','f','h']
Graph['h'] = ['g']

# Classe Maillon
class Maillon : 
    
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

# Classe Pile
class Pile:

    def __init__(self):
        self.taille = 0 # Nombre d'assiettes dans la pile
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

# Fonction de parcours
def dfs(graph, s):
    """
        #### Paramètres ####
            graph :
                Modelisation du graphe a etudier.

            s :
                Sommet actuel.

        #### Variables ####
            Pere :
                Dictionnaire tel que, en fin de parcours, pour tout sommet 's' du graphe, Pere['s']
                sera le pere de 's', c'est a dire le sommet a partir duquel 's' a ete decouvert lors
                du parcours.

            queue :
                Liste utilisée comme pile (LIFO).

    """

    Pere, queue = {s : None}, Pile()
    queue.empiler(s)

    while not(queue.est_vide()):
        u = queue.lire_sommet()
        R = [y for y in graph[u] if y not in Pere]
        if R:
            v = random.choice(R)
            Pere[v] = u
            queue.empiler(v)
        else:
            queue.depiler()

    return Pere


if __name__ == "__main__":
    print(dfs(Graph, 'g'))