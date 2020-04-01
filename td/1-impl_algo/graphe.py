"""
    Declaration des graphes du TD.
"""

graphe_1 = dict()
graphe_1['a'] = ['b', 'c', 'h']
graphe_1['b'] = ['a', 'i']
graphe_1['c'] = ['a', 'd', 'e']
graphe_1['d'] = ['c', 'e']
graphe_1['e'] = ['c', 'd', 'g']
graphe_1['f'] = ['g', 'i']
graphe_1['g'] = ['e', 'f', 'h']
graphe_1['h'] = ['a', 'g', 'i']
graphe_1['i'] = ['b', 'f', 'h']

if __name__ == "__main__":
    for key, values in graphe_1.items():
        print(key, '->', values)