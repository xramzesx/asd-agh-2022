# Jakub Kędra
##### OPIS ALGORYTMU #####
# Korzystając z sugestii z wykładu, w celu posortowania tablicy T wykorzystałem algorytm sortowania kubełkowego
# W swojej implementacji w celach optymalizacyjnych każdy z kubełków reprezentowany jest przez zakres [a,b] w tablicy
# wynikowej (result).
# 
# Struktura kubełka:
# - Początkowy index kubełka przechowuje w tablicy [starts];
# - Ostatni index ( a raczej pierwszy nienależący index ) [ends];
# 
# Do bucket sortu potrzebowaliśmy znaleźć max i min możliwe wartości. W tym celu skorzystałem z tablicy P, wyciagając 
# prosto z nich szukane min_v i max_v
# 
# Sam algorytm jest nieco zmodyfikowanym algorytmem sortowania przez zliczanie zaprezentowanym podczas wykładu.
# W odróżnieniu od counting sortu, indexy konkretnych kubełków (liczników) wyliczam za pomocą wzoru:
# 
#   index = ( number - min ) / ( max - min ) * n
# 
# Gdzie:
#   number - i-ta liczba z tablciy T[i]
#   min, max - skrajne wartości, znalezione wcześniej
#   n - długość tablicy T 
# 
# A w celu posortowania kubełków skorzystałem z prostego sortowania przez wstawianie, ponieważ dla optymistycznych danych
# potrafi on osiągnąć złożoność O(n) oraz lepiej sprawdza się dla tablic o małej liczbie elementów od innych szybkich algorytmów
# 

##### ZŁOŻONOŚĆ #####
# Obliczeniowa:
#   Najlepszy przypadek: O(n)
#   Średni przypadek: O(n + k)
#   Najgorszy przypadek: O(n^2)
# 
# Pamięciowa:
#   O(3*n) = O(n)
# 
# Gdzie:
#   n - długość tablicy T
#   k - długość tablicy P
# 

##### IMPORTY #####

from zad3testy import runtests

##### FUNKCJE POMOCNICZE #####

# poszukiwanie max przedziału [a , b]
def min_max ( arr ):
    min_v = arr[0][0]
    max_v = arr[0][1]

    for a, b, _ in arr:
        if a < min_v:
            min_v = a
        if b > max_v:
            max_v = b

    return min_v, max_v


def generate_index( n, min_v, max_v ):
    multipler = ( n - 1 ) / ( max_v - min_v )

    def index ( number ) : return int ( ( number - min_v ) * multipler )

    return index

##### FUNKCJE SORTUJĄCE #####

# szybki algorytm sortowania małych tablic [start, end)
def insert_sort ( arr, start, end ):
    for i in range( start + 1, end ):
        element = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > element:
            arr[ j + 1 ] = arr[ j ]
            j -= 1
        
        arr[j + 1] = element

# sortowanie kubełkowe ( główna część programu )
def bucket_sort ( arr, min_v, max_v ):
    n = len( arr )
    
    # indexy kubełków
    index = generate_index( n, min_v, max_v )
    
    # deklaracja kubełków
    starts = [ 0 ] * n
    ends = [ 0 ] * n

    # tablica wynikowa
    result = [ 0 ] * n

    # zliczanie kubełków
    for number in arr:
        ends[ index( number ) ] += 1

    starts [0] = ends[0]

    # odpowiednie nadanie indexów 
    # krańcowym wartością kubełków
    for i in range( 1, n ):
       ends[ i ] += ends [ i - 1 ]
       starts [ i ] = ends[ i ]

    # przepisanie elementów z arr do result
    # do konkretnych przedziałów z kubełków,
    # a następnie posortowanie ich
    for i in range ( n - 1, -1, -1 ):
        j = index( arr[ i ] )

        result [ starts[ j ] - 1 ] = arr[ i ]
        starts [ j ] -= 1

        if starts [j] == 0 or starts[ j ] == ends[ j - 1 ]:
            insert_sort( result, starts[ j ], ends[ j ] )

    return result



def SortTab(T,P):
        
    # Szukamy końcowych fragmentów przedziałów
    min_v, max_v = min_max( P )

    return bucket_sort( T, min_v, max_v )

runtests( SortTab )