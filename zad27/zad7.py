# Jakub Kędra
####### OPIS ############################################################
# 
# Rozwiązaniem tego zadania jest tak naprawde znalezienie cyklu
# hamiltona wewnątrz grafu z krawędziami warunkowymi (wejście z jednej
# strony, wyjście z drugiej).
# 
# W tym celu korzystam z algorytmu wykorzystującego DFS z backtrackingiem
# Jeśli uda się znaleźć taki cykl, zwraca go. Jeśli na którymkolwiek
# z etapów nie uda się poprowadzić ścieżki dalej, algorytm cofa się
# do ostatniego miejsca w którym może podjąć jeszcze inną decyzje
# 
#### ZŁOŻONOŚĆ ###########################################################
# BEST: O(n)
# WORST: O(n!)

from zad7testy import runtests

def droga( G ):

    # constants:
    n = len(G)

    north = 0
    south = 1

    # caching:
    path = []
    parents = [ None ] * n
    entrances = [ None ] * n
    visited = [ False ] * n

    # edge cases:
    parents[0] = 0
    entrances[0] = north
    visited[0] = True
    
    def get_entrance ( u, v ):
        return south if u in G[v][north] else north

    def dfs_visit (u, entrance = None):
        nonlocal path
        visited[u] = True
        path.append(u)
        if entrance == None:
            entrance = get_entrance( parents[u], u )

        for v in G[u][entrance]:
            if not visited[v]:
                parents[v] = u
                if dfs_visit( v ):
                    return True
                parents[v] = None
        
        if len(path) == len(G) and 0 in G[u][entrance] and u in G[0][south]:
            return True

        visited[u] = False
        path.pop()
        return False

    return path if dfs_visit(0, north) else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )