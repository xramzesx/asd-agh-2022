# Jakub Kędra

##### OPIS #########################################################################
# 
# W rozwiązaniu zadania 1. wykorzystałem kilka algorytmów sortowania.
# 
# - Dla dużych k (>12) korzystam z implementacji sortowania przez kopcowanie,
#   o złożoności obliczeniowej O(nlog(k)) i pamięciowej O(k) poprzez utworzenie
#   kopca na min(k + 1, n) pierwszych elementów, a następnie zdejmowaniu pierwszego
#   elementu z niego i dodawanie kolejnego nieposortowanego elementu do niego
# 
# - Dla k <= 12 wykorzystuje algorytm sortowania przez wybór ( obl. O( n*k ); pam. O(1) ) 
#   Liczba 12 została wyznaczona doświadczalnie, podczas testów.
# 
# - Dla k == 1, wykorzystuje dosłownie jedną iterację uproszczonego sortowania bąbelkowego
#   Pozwala to uzyskać złożoność obliczeniową O(n) oraz pamięciową O(1)
# 
# Poszczególne algorytmy okazywały się być szybsze dla poszczególnych
# zakresów argumentu k

##### ZŁOŻONOŚĆ ############################
# 
# - ogólna złożoność:
#   obliczeniowa : O(n*log(k))
#   pamięciowa   : O(k)
# 
# - dla k = Θ(1):
#   obliczeniowa : O(n)
#   pamięciowa   : O(1)
#   * tylko dla k = 1  
# 
# - dla k = Θ(log n) :
#   obliczeniowa : O(n*logn)
#   pamięciowa   : O(k)
#   * dla k > 12
# 
# - dla k = Θ(n):
#   obliczeniowa : O (n^2)
#   pamięciowa   : O(1)
#   * dla k > 1 oraz k < 12
# 

##### IMPORT #####

from zad1testy import Node, runtests

#### PORUSZANIE SIĘ PO KOPCU ####

def left( i ): return 2*i + 1
def right( i ): return 2*i + 2
def parent( i ): return (i - 1) // 2


#### NAPRAWY KOPCA ####

# naprawa kopca w dół
# (i-ty element jest popsuty)
def heapify_down ( heap, n, i ):
    l = left(i)
    r = right(i)

    min_ind = i

    if l < n and heap[l].val < heap[min_ind].val:
        min_ind = l

    if r < n and heap[r].val < heap[min_ind].val:
        min_ind = r

    if min_ind != i:
        heap[i], heap[min_ind] = heap[min_ind], heap[i]
        heapify_down(heap, n, min_ind)

# naprawa kopca w góre
# (i-ty element jest zepsuty)
def heapify_up( heap, i):
    p = parent(i)
    if i > 0 and heap[p].val > heap[i].val:
        heap[p], heap[i] = heap[i], heap[p]
        heapify_up(heap, p)


# utworzenie nowego kopca
def build_heap( heap, n ):
    for i in range( parent( n - 1 ), -1, -1 ):
        heapify_down( heap, n, i)


##### OPERACJE NA KOPCU #####

# odrywanie ostatniego
# (tu: najmniejszego) elementu
def heap_pop(heap, i):
    result = heap[0]
    heap[0], heap[i] = heap[i], heap[0]
    heapify_down( heap, i, 0 )

    return result

# dodawanie nowego elementu 
def heap_push(heap, node, n):
    heap[n - 1] = node
    heapify_up(heap, n - 1 )


##### OPERACJE NA NODE'ACH ######

# zakładamy, że prev_i != None
# oraz prev_i.next != None
def swap_node( prev_a, prev_b ):
    a, b = prev_a.next, prev_b.next
    
    prev_a.next = b
    prev_b.next = a

    a.next, b.next = b.next, a.next


#### SORTOWANIA #####

# dla k = 1, O(n)
# jest to pojedyncza iteracja w stylu bubble sortu
def bubble_iter(p):
    first = Node()

    first.next = p

    if p.val > p.next.val:
        swap_node(first, p)
    
    prev_a = first
    prev_b = first.next


    while prev_b.next != None:
        if prev_b.val > prev_b.next.val:
            swap_node(prev_a, prev_b)

        prev_a = prev_a.next
        prev_b = prev_a.next

    return first.next

# Sortowanie przez wybór, O(n*k)
# (okazuje się być szybsze od heapsortu dla k <= 12)
def select_sort(p, k):
    first = Node()
    first.next = p

    prev_a = first

    while prev_a.next != None:
        
        i = 0
        prev_min = prev_a
        prev_b = prev_a.next

        changed = False    
        
        while prev_b.next != None and i < k:

            if prev_min.next.val > prev_b.next.val:
                prev_min = prev_b
                changed = True

            prev_b = prev_b.next
            i += 1
        
        if changed:
            swap_node( prev_a, prev_min )

        prev_a = prev_a.next


    return first.next

def heap_sort( p, k ):

    k1 = 0
    roll = p

    # tworzymy kopiec na pierwsze k + 1 elementów
    heap = [ None for _ in range( k + 1 ) ]

    # wpisujemy kolejne elementy listy do tablicy pomocniczej
    while k1 < k + 1 and roll != None:
        heap[k1] = roll
        roll = roll.next
        k1 += 1

    # budujemy kopiec
    build_heap( heap, k1 )

    result = Node()
    rtmp = result

    # dla kolejnych elementów z po za stosu wykonujemy
    # kolejne kopcowania
    while roll != None:
        rtmp.next = heap_pop( heap, k1 - 1 )
        rtmp = rtmp.next

        heap_push( heap, roll, k1 )
        roll = roll.next

    # opróżniamy reszte kopca
    for i in range( k1 ):
        rtmp.next = heap_pop( heap, k1 - 1 - i )
        rtmp = rtmp.next

    # przerywamy potencjalny cykl
    if rtmp != None:
        rtmp.next = None

    return result.next

# main
def SortH(p,k):
    
    # rozpatrujemy kilka przypadków
    if k == 0: return p
    if p == None or p.next == None:
        return p
    
    # O(n)
    if k == 1:
        return bubble_iter(p)

    # O(n*k)
    if k <= 12:
        return select_sort ( p, k )

    # O(n*log(k))
    return heap_sort( p, k )

runtests( SortH ) 
