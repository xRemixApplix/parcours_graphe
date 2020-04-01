"""
    Script de parcours en largeur du graphe.
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

    couleur = dict()
    list_file = []
    list_parcours = []

    # Initialisation de la couleur de chaque sommet a 'blanc'
    for i in graphe:couleur[i] = 'blanc'

    couleur[s] = 'noir'
    list_file.append(s)
    list_parcours.append(s)

    while list_file:
        u = list_file[0]
        list_file = list_file[1:]
        for v in graphe[u]:
            if couleur[v] != 'noir':
                couleur[v] = 'noir'
                list_file.append(v)
                list_parcours.append(v)

    return list_parcours
        

    
if __name__ == "__main__":
    print(parcours_graphe('a', graphe.graphe_1))