# Jakub Kędra
# Najmniejsza wymagana liczba postojów
##### OPIS ############################
# 
# Jest to algorytm dosyć prosty. Z perpektywy cysterny, musimy wypuścić najpierw drona,
# który będzie naszym zwiadowcą. Dron nie pobiera żadnej energii, lecz posłuży on
# Maksymilianowi jako cenne źródło informacji.
# 
# Dron kieruje się wzdłuż trasy cysterny i zbiera informacje o wielkościach mijanych 
# kałuż z ropą w postaci krotki ( fuel, index ). W trakcie przelotu, symuluje również 
# na bieżąco zużycie paliwa przez cysternę. 
# Jeśli wskaźnik paliwa zejdzie do 0, inteligentne systemy drona wyciągają informację
# o dotychczasowej największej plamie ropy, która jeszcze nie została wykorzystana,
# a następnie miejsce jej położenia (w postaci indexu) dodaje do tablicy, którą ma
# zwrócić Maksymilianowi
# 
# Po dotarciu do miasta B, dron zwraca zdobyte informacje o najoptymalniejszych
# kałużach, w międzyczasie sortujac je rosnąco tak, aby Maksymilian mógł się łatwo
# w otrzymanym wyniku połapać.
# 
# Tym dronem bedzie nasza funkcja plan(T), a inteligentnymi systemami drona będzie
# kopiec, w postaci kolejki priorytetowej
#
#### DOWÓD POPRAWNOŚCI ####################
# 
# Na starcie tankujemy paliwo na polu 0.
# Nie potrzebujemy tankować na każdym z przystanków, jak również nie potrzebujemy 
# wykorzystać całego zdobytego paliwa. Żeby przejechać jak największy dystans
# bez zatrzymywania się, potrzebujemy zbierać tylko największe z aktualnie
# dostępnych mijanych złóż ropy. W tym celu wykorzystujemy kolejke priorytetową,
# dzięki której możemy w czasie logk otrzymać dodać nowe pole do kolejki oraz 
# wyciągnąć maksymalnie dostępne z nich prosto z niej.
# 
# Dlatego też takie podejście zapewnia nam dostęp zwrócenie informacji tylko
# o wymaganych postojach.
# 
###### ZŁOŻONOSĆ ###########################
# BEST:  O(n + nlogn)     = O(nlogn)
# AVG:   O(nlogk + nlogn) = O(nlogk + nlogn)
# WORsT: O(nlogn + nlogn) = O(nlogn)
# 
# gdzie:
#   k - liczba niezerowych pól
#   n - liczba wszystkich elementów tablicy
# oraz:
#   0 <= k <= n
# 

### ALGORYTM ###############################

#### IMPORTY ###############################
from queue import PriorityQueue
from zad5testy import runtests

#### KOD ###################################
def plan(T):
    que = PriorityQueue()
    
    n = len(T)

    result = [0]
    fuel = T[0]
    
    for i in range( 1, n - 1 ):
        fuel -= 1
        if T[i] != 0:
            que.put( ( -T[i], i ) )

        if fuel <= 0:
            f, index = que.get()
            fuel = -f
            result.append(index)

    return sorted( result )


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )