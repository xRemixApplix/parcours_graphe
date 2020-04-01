"""
    Script de parcours en profondeur recursif du graphe.
"""

import graphe

def parcours_graphe(s, graphe):
    """
        Fonction de parcours en largeur du graphe.
            s :
                Sommet de départ du parcours.
            graphe :
                Graphe a parcourir.
    """
    couleur[s] = 'noir'
    print(s)

    listing = [y for y in graphe[s] if couleur[y] == 'blanc']

    for i in listing:
        if couleur[i] == 'blanc':parcours_graphe(i, graphe)

    
if __name__ == "__main__":
    couleur = dict()
    list_parcours = []

    # Initialisation de la couleur de chaque sommet a 'blanc'
    for i in graphe.graphe_1 : couleur[i] = 'blanc'

    print(parcours_graphe('a', graphe.graphe_1))
