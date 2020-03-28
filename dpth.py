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

    Pere, queue = {s : None}, [s]

    while queue:
        u = queue[-1]
        R = [y for y in graph[u] if y not in Pere]
        if R:
            v = R[0]
            Pere[v] = u
            queue.append(v)
        else:
            queue.pop()
    return Pere


if __name__ == "__main__":
    print(dfs(Graph, 'g'))