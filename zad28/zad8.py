# Jakub Kędra
#### OPIS #####################
# Potrzebujemy wygenerować wszystkie krawędzie w grafie pełnym
# Następnie sortujemy krawędzie po wagach
# 
# Będzie nas interesować tylko taki spójny podzbiór tych krawędzi, który
# jest większy niż V - 1 krawędzi
# 
# Następnie szukamy spójnego podgrafu, o najmniejszej różnicy wag krańcowych krawędzi
# Zatem poruszamy się po wszystkich wygenerowanych krawędziach w sposób podobny do metodu
# sliding window
#  
#### ZŁOŻONOŚĆ ##########################
# O( E * V ) lub O( V*(V - 1) )
# 
#### IMPLEMENTACJA ######################

#### IMPORTY ####

from collections import deque
from math import ceil, sqrt
from zad8testy import runtests

#### KOD ####

# O(V + E)
def is_consistent( G ):
    q = deque()
    
    visited = [False] * len(G)
    
    q.appendleft( 0 )

    while q:
        u = q.pop()
        for v in G[u]:
            if not visited[ v ]:
                visited[v] = True
                q.appendleft( v )

    for v in visited:
        if not v:
            return False
    return True

def edge_len( a, b ):
    xa, ya = a
    xb, yb = b

    return ceil(sqrt(( xa - xb ) ** 2 + (ya - yb) ** 2))

def highway( A ):
    edges = []
    n = len(A)

    # O(V^2)
    # generujemy wszystkie krawędzie
    for i in range( n ):
        for j in range( i + 1,  n ):
            edges.append( ( edge_len( A[i], A[j] ), i, j ) )

    # sortujemy malejąco po odległościach
    # edges.sort( key= lambda x : x[0], reverse=True )
    edges.sort( key= lambda x : x[0], reverse=True )
    
    G = [ deque() for _ in A ]
    
    # tworzymy listę sąsiedztwa dla V - 1 elementów
    for k in range( n - 1 ):
        value, i, j = edges[k]
        G[i].append( j )
        G[j].append( i )


    # inicjalizujemy zakres
    start = 0
    end = n - 2

    # oraz najmniejszą różnicę
    difference = float('inf')
    
    # O( V * E )
    while end < len( edges ):
        current_diff = edges[start][0] - edges[end][0]

        if end - start >= n - 2 and is_consistent( G ):
            if current_diff < difference:
                difference = current_diff
            
            value, i, j = edges[start]
            G[i].popleft()
            G[j].popleft()
            start += 1
        else:
            end += 1
            if end < len(edges):
                value, i, j = edges[end]
                G[i].append( j )
                G[j].append( i )

    return difference 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )