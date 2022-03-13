# Jakub Kędra
##### OPIS #####
# 
# Chcąć najszybciej znaleźć maksymalny poziom "c" najpierw sortuje 
# tablice po długości przedziałów (b - a) malejąco.
# W tym algorytmie skorzystamy z faktu, że każdy nowonapotkany rozłączny 
# przedział w posortowanej tablicy będzie największym z przedziałów 
# w swoim zakresie.
# 
# Następnie tworzę linked listę/kolejkę, do której będę umieszczał 
# największe rozłączne zakresy i umieszczam pierwszy element 
# posortowanej tablicy na jej początku
# 
# Iteruję resztę tablicy, jeśli należy do któregoś z zewnętrznych 
# przedziałów, inkrementuję jego licznik, jeśli nie należy do żadnego, 
# dodaje go do wcześniejszej linked listy.
# 
# I na sam koniec iteruje linked liste w poszukiwaniu największego z 
# liczników i go potem zwracam 
# 
##### ZŁOŻONOŚĆ OBLICZENIOWA #####
# 
# W optymistycznym przypadku:
#   O(nlogn + n)
# gdzie nlogn wynika z korzystania z quicksortu, a n z osobnej pętli
# W pesymistycznym przypadku:
#   O(n^2 + n^2)
# gdzie pierwsze n^2 wynika z quicksortu, a drugie z przypadku, w którym
# żadne z 2 elementów listy nie zawierają się w sobie
# 
##### IMPORTY #####

from zad2testy import runtests

##### STRUKTURA KOLEJKI #####

class Node:
    def __init__(self, rang = None, next = None) -> None:
        self.counter = 0
        self.range = rang
        self.next = next
        pass

##### FUNKCJE POMOCNICZE #####

def compare_range(outer, inner):
    start_o, end_o = outer
    start_i, end_i = inner

    return start_o <= start_i and end_i <= end_o

##### QUICKSORT #####

def partition ( arr, left, right ):
    x = arr[ right ][ 1 ] - arr[ right ][ 0 ]

    i = left - 1

    for j in range( left, right ):
        if arr[ j ][ 1 ] - arr[ j ][ 0 ] >= x:
            i += 1
            arr[ i ], arr[ j ] = arr[ j ], arr[ i ]
    
    arr[ i + 1 ], arr[ right ] = arr[ right ], arr[ i + 1 ] 
    
    return i + 1

def quick_sort ( arr, left, right ):

    if left < right:
        pivot = partition( arr, left, right )
        quick_sort( arr, left, pivot - 1 )
        quick_sort( arr, pivot + 1, right )


##### MAIN #####

def depth(L):
    
    # sortujemy malejąco po długościach przedziałów
    quick_sort(L, 0, len(L) - 1)

    # tworzymy kolejke na największe rozłączne zakresy
    # (nadzakresy)
    first = Node()
    first.next = Node( L[0] )

    # zliczamy ilości podzakresów wszystkich nadzakresów
    for i in range(1, len(L) ):
        roll = first
        changed = False

        while roll.next != None:
            if compare_range(roll.next.range, L[i] ):
                roll.next.counter += 1
                changed = True
                break
            roll = roll.next

        if not changed:
            roll.next = Node( L[i] )

    
    roll = first
    max_counter = 0

    # szukamy max z liczników
    while roll.next != None:
        max_counter = max( max_counter, roll.next.counter )
        roll = roll.next
        
    return max_counter

runtests( depth ) 
