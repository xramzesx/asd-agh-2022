# Jakub Kędra
#### OPIS ####
# Najpierw dla każdego pojedynczego wierzchołka nadajemy dystans od wierzchołka początkowego s.
# W tym celu wykorzystujemy zwykły algorytm BFS. W tym wypadku wystarczy tylko znaleźć wszystkie
# wierzchołki w promieniu minimalnej odległości pomiędzy punktami s oraz t.
# 
# Następnie, jesli w ogóle oba wierzchołki s i t znajdują się przynajmniej w spójnym podgrafie,
# będziemy próbować odtwarzać wszystkie możliwe najkrótsze ścieżki. 
# 
# Dla każdegej i-tej wartości dystansu od 0 do distance[t] zliczamy ile jest możliwych 
# wierzchołków o i-tym dystansie oraz przez które możemy się dostać z wierzchołka s do t ( i na odwrót ).
# 
# Po zliczeniu, interesuje nas tak naprawde tylko "most", tj. tylko spójny 2-elementowy podciąg, którego 
# obie wartości są równe 1. Taki podciąg mówi nam o tym, że pomiędzy dwoma odległościami istnieje tylko jedna
# możliwa krawędź. Ta właśnie krawędź, jeśli zostanie usunięta, przerwie nam najkrótszą ścieżkę
# 
#### UZASADNIENIE ####
# [Zakładamy, że odległość pomiędzy dwoma punktami, należacymi do dwóch niespójnych podgrafów grafu wynosi nieskończoność]
# 
# Usunięcie krawędzi, nie należących do żadnej najkrótszej ścieżki nie wpływa kompletnie na wynik końcowy.
# Zatem będą nas tylko interesowały wierzchołki i krawędzie należące do przynajmniej jednej z najkrótszych ścieżek.
# Wybrane wierzchołki możemy pogrupować, ze względu na odległość od wierzchołka s. Jeśli pomiędzy dwoma wierzchołkami 
# o różnych odległościach występuje tylko jedna krawędź, usunięcie jej spowoduje wydłużenie najkrótszej ścieżki w całym
# grafie, ponieważ istnienie takiej krawędzi mówi nam tak na prawdę o tym, że każda z potencjalnych najkrótszych ścieżek
# zbiega się właśnie do tej krawędzi ( jest ona mostem ).
# 
# Pomiędzy dwoma sąsiednimi grupami występuje dokładnie jedna krawędź wtw, gdy w obu tych grupach znajduje się dokładnie po
# jednym wierzchołku. Wynika to z faktu takiego, że każdy wierzchołek danej grupy musi mieć połączenie z przynajmniej jednym 
# wierzchołkiem obu sąsiednich grup.
# 
#### ZŁOŻONOŚĆ ####
# Obliczeniowa:
#   Θ ( v + e )
# Pamięciowa:
#   O( v )
# gdzie:
#   v - liczba wierzchołków
#   e - liczba krawędzi
#  
#### IMPLEMENTACJA ####

#### IMPORTY ####

from collections import deque
from zad6testy import runtests

#### KOD ####

def longer( G, s, t ):
    if s == t: return None

    n = len(G)
    q = deque()

    # prepare arrays
    visited = [False] * n
    distances = [-1] * n
    
    # setting up first BFS
    visited[s] = True
    distances[s] = 0

    q.append( s )

    #### BFS -> count distances ####

    min_distance = float('inf')
    
    while q:
        u = q.popleft()
        if distances[u] > min_distance:
            continue
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1  
                if v == t:
                    min_distance = distances[v]
                q.append(v)

    # print( min_distance, distances[t] )

    # graf nie jest spójny
    if distances[t] == -1:
        return None


    #### BFS -> count all nodes with specific distances ####

    # setting up second BFS 
    q.append( t )
    max_distance = distances[t] + 1
    
    visited[t] = False
    nodes = [ 0 ] * max_distance
    lasts = [-1 ] * max_distance
    
    while q:
        u = q.popleft()
        nodes[ distances[u] ] += 1
        lasts[ distances[u] ] = u

        for v in G[u]:
            if visited[v] and distances[u] == distances[v] + 1:
                visited[v] = False
                q.append( v )

    ### Searching for 2 adjacent buckets with only 1 node ###

    for i in range( 1, max_distance ):
        if nodes[i - 1] == nodes[i] and nodes[i] == 1:
            return ( lasts[i - 1], lasts[i] )

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )