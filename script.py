Graph = dict()
Graph['a'] = ['b','c']
Graph['b'] = ['a','d','e']
Graph['c'] = ['a','d']
Graph['d'] = ['b','c','e']
Graph['e'] = ['b','d','f','g']
Graph['f'] = ['e','g']
Graph['g'] = ['e','f','h']
Graph['h'] = ['g']

for key, values in Graph.items():
    print(key, '->', values)