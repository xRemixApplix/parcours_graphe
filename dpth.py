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

def dfs(Graph, s):
    """
        #### Paramètres ####
            Graph :
                Modelisation du graphe a etudier.

            s :
                Sommet actuel.

        #### Variables ####
            couleur :
                Dictionnaire tel que pour tout sommet 's', couleur['s'] soit blanc si le sommet 's'
                n'est pas dans la file, gris si le sommet est dans la file et noir si le sommet est
                sorti de la file.

            Pere :
                Dictionnaire tel que, en fin de parcours, pour tout sommet 's' du graphe, Pere['s']
                sera le pere de 's', c'est a dire le sommet a partir duquel 's' a ete decouvert lors
                du parcours.

            queue :
                Liste utilisée comme pile (LIFO).

    """

    # Definition et initialisation du dictionnaire representant la couleur de chaque sommet 
    couleur = dict()
    for v in Graph:
        couleur[v] = 'blanc'

    # Definition et initialisation du dictionnaire representant le pere de chaque sommet lors du parcours
    Pere = dict()
    Pere[s] = None

    # Prise en compte passage par le sommet
    couleur[s] = 'gris'

    # Ajout du sommet dans la pile
    queue = [s]

    while queue:
        u = queue[-1]
        R = [y for y in Graph[u] if couleur[y] == 'blanc']
        if R:
            v = R[0]
            couleur[v] = 'gris'
            Pere[v] = u
            queue.append(v)
        else:
            queue.pop()
            couleur[u] = 'noir'
    return Pere


if __name__ == "__main__":
    print(dfs(Graph, 'a'))