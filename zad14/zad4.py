# Jakub Kędra
####### ZŁOŻONOŚĆ ########################
# BEST : O(nlogn + n)
# WORST: O(nlogn + n*n)
####### OPIS #############################
# 
# Swoje rozwiązanie zaczynam od posortowawnia tablicy T po końcach przedziałów.
# Taki porządek tablicy pozwoli nam na łatwe znajdowanie przecięć pomiędzy przedziałami.
# 
# Następnie zliczam dla każdego i-tego elementu tablicy jego pojemność ze wzoru:
#   capacity = h * ( b - a )
# 
# Teraz przechodzimy do głównej części zadania. Potrzebujemy znaleźć taki niekoniecznie spójny
# ciąg przedziałów, który nie koliduje ze sobą oraz który mieści się w cenie P
# 
# W tym celu tworzymy tablicę F[n][P + 1], Każdy element F[i][p] zawiera informację o 
# maksymalnej możliwej do osiągniecia dodatkowej pojemności w cenie nie przekraczającej p,
# rozpoczynając z i-tego elementu.
# 
# Każdy obliczony element tablicy F jest przechowywany w postaci krotki:
#   ( capacity, next_element ), 
# dzięki której jesteśmy w stanie odtworzyć kolejność najlepszego z rozwiązań
# 
# Nie wszystkie wartości w tablicy będą obliczone, także zamiast niej można było wykorzystać słownik,
# lecz na potrzeby warunków zadań trzymamy się konwencji z tablicą.
# 
#### Zasada działania głównej części rozwiązania:
# 
# Iterujemy całą tablicę T. Dla każdego z jej elementów sprawdzamy czy po pierwsze nie jest on za drogi,
# a po drugie, szukamy rekurencyjnie jaką maksymalną pojemność może nam dać wraz ze swoimi następnikami.
# 
# W celu ograniczenia liczby obliczeń, powtarzające się wartości zwracamy na starcie rekurencji.
# Następnie dla każdego j-tego elementu (gdzie i + 1 <= j < n ) sprawdzamy, czy nie koliduje z i-tym oraz
# czy j-ty element nie jest zbyt drogim elementem. Jeśli nie, robimy dokładnie to samo dla j-tego elementu,
# co dla i-tego, a następnie zapisujemy najlepszy z wyników (pojemności) w tablicy F
# 
# Na końcu naszych obliczeń zawsze szukamy największej z pojemności oraz index zapisujemy do pierwszego 
# elementu ścieżki.
# 
# Na podstawie zapisanej struktury krotek wewnątrz tablicy F jesteśmy teraz w stanie odtworzyć całą naszą ścieżkę,
# w stylu nieco przypominającym linked-listę.
# 
# I na samym końcu zwracamy najbardziej optymalną ścieżkę.
#
#### Dodatkowe info #####################
# 
# - Tak naprawdę sortowana nie jest tablica T, lecz jej indexy, przechowywane w tablicy indexes[n]
# 


#### KOD ####

from zad4testy import runtests

#### FINDING BEST SUBSET ####

def check( T, F, ind, caps, i, p ):
    _i = ind[ i ]

    # if already computed, return it
    if F[ _i ][p] != -1:
        return F[ _i ][p][0]

    # constants
    n = len(T)
    start = 1
    end = 2
    price = 3
    
    # max_capacity
    max_c = 0

    # next node
    next_i = -1

    # check next dorms, if fits
    for j in range( i + 1, n ):
        _j = ind[ j ]
        
        if T[ _i ][end] >= T[ _j ][start] or T[ _i ][price] + T[ _j ][price] > p:
            continue

        curr_c = check ( T, F, ind, caps, j, p - T[ _i ][price] )

        if curr_c > max_c:
            max_c = curr_c
            next_i = j


    capacity = max_c + caps[ _i ]

    # save computed result
    F[ _i ][p] = ( capacity , next_i )
    
    return capacity


#### MAIN PART ####
 
def select_buildings(T,P):

    # constants:
    n = len( T )
    start = 1
    end = 2
    price = 3

    # sort by end of range
    indexes = sorted ( [ i for i in range( n ) ], key = lambda i : T[i][end] )

    # compute capacities of dormitories
    capacities = [ h * ( b - a ) for h, a, b, w in T ]

    # declare 
    F = [ [ -1 for p in range( P + 1 ) ] for i in range( n ) ]


    # for recreating path
    max_c = 0
    max_i = 0

    for i in range( n ):
        if T[indexes[i]][price] > P:
            continue
        
        curr_c = check( T, F, indexes, capacities, i , P )

        if curr_c > max_c:
            max_c = curr_c
            max_i = i

    # recreate path
    result = []
    
    next_i = max_i
    p = P

    while next_i != -1 and F[ indexes[ next_i ]][p] != -1:
        _i = indexes[ next_i ]
        result.append( _i )
        next_i, p = F[ _i ][p][1], p - T[_i][price]

    return result

#### TESTS ####
runtests( select_buildings )