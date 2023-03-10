# Jakub Kędra
##### OPIS ############################
# 
# Jest to algorytm nieco zachłanny. Pierwszym miastem zawsze jest jeden z sąsiadów źródla S,
# drugim natomiast dowolne miasto, nie będące już wybranym miastem ani nie będące źródłem S.
# 
# W celu znalezienia maksymalnego przepływu dla dwóch wybranych miast, potrzebne nam jest utworzenie
# tzw. "super ujścia", czyli dodatkowego wierzchołka, do którego prowadzą dwie ściezki o przepustowości inf
# prosto z tych dwóch wybranych miast.
# 
# Dla każdej tak przygotowanej pary puszczamy algorytm znajdowania największej wartości przepływu Edmunda-Karpa,
# wykokrzystujący BFS oraz szukamy największego z nich.
# 
#### ZŁOŻONOŚĆ ########################
# 
# O( V^2*E + V*E^2 )
# 
#### IMPLEMENTACJA ####################

from collections import deque
from zad9testy import runtests

def find_path ( G, F, s, t ):
    
    n = len(G)
    
    q = deque()
    q.append( s )

    parents = [ -1 ] * n
    visited = [False] * n

    visited[s] = True


    while q:
        v = q.popleft()
        for i in range( len( G[v] ) ):
            u, capacity = G[v][i]
            flow = F[v][i]

            if not visited[u] and capacity - flow > 0:
                visited[u] = True
                parents[u] = ( v, i )

                if u == t:
                    return parents
                
                q.append( u )

    return []


def find_maxflow( G, s, t ):

    F = [ [ 0 for u in G[v] ] for v in range( len(G) ) ]
    path = find_path( G, F, s, t )

    # constants
    vertex = 0
    capacity = 1


    while path:
        u = t
        flow = float('inf')
        while path[u] != -1:
            v, i = path[u]
            flow = min( flow, G[v][i][capacity] - F[v][i] )
            u = v

        u = t
        while path[u] != -1:
            v, i = path[u]
            F[v][i] += flow
            u = v
        path = find_path( G, F, s, t )
    
    return sum ( F[s] )

def maxflow( edges , s ):

    edges.sort(key= lambda x : x[2], reverse = True)

    n = max( max( edges, key=lambda x: x[0] )[0], max( edges, key=lambda x: x[1] )[1] ) + 1

    # +1 dla super wyjścia
    G = [ deque() for _ in range( n + 1 ) ]
    # G = [ [] for _ in range( n + 1 ) ]

    for v, u, capacity in edges:
        G[v].append( ( u, capacity ) )


    super_edge = ( n, float('inf') )

    max_flow = 0

    for v, _ in G[s]:
        
        G[v].appendleft( super_edge )

        for u in range( n ):
            if u == v: continue
            if u == s: continue

            G[u].appendleft( super_edge )

            max_flow = max( find_maxflow( G, s, n ), max_flow )

            G[u].popleft()
        G[v].popleft()
    
    return max_flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )