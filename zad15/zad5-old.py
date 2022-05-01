# Jakub Kędra
from zad5testy import runtests



def print_arr( arr ):
    for r in arr:
        for c in r:
            print(f"{c}\t", end="")
        print()


def check ( T, F, i, fuel, s = 1):
    n = len(T)
    
    min_v = n
    next_i = -1
    next_f = -1
    # if fuel < 0: return 0

    # for j in range ( i + T[i], i, -1 ):
    #     if T[j] == 0 or fuel - ( i - j ) + T[j] :
    #         continue
        
        

    #     curr_v = check( T, F, j, fuel - j + T[j])

    # (0, fuel]

    # print( "-"*s,  i, "\t", fuel, "\t", s)
    if fuel + i >= n - 1:
        # print('ja', fuel + i, n)
        return s

    steps = 0

    if F[i][ i + fuel ] != -1:
        return F[i][ i + fuel ][ steps ]

    for step in range( fuel, 0, -1 ):
        j = step + i
        
        if j >= n: break

        _fuel = fuel - step + T[j]
        if T[j] == 0 or _fuel < 0:
            continue


        curr_v = check( T, F, j, _fuel, s + 1 )
        
        if min_v > curr_v:
            min_v = curr_v
            next_i = j
            next_f = _fuel
    
    F[i][ fuel + i ] = ( min_v, next_i, next_i + next_f )    
    return min_v

def plan(T):

    # print(T)
    n = len(T)

    # F[ index ][ fuel ] = ( min_steps, remaining_fuel, next_i )

    F = [ [ -1 for fuel in range( n ) ] for i in T ]

    min_v = check( T, F, 0, T[0] )
    
    print(min_v)

    index = 1
    fuel = 2

    next_i = 0
    next_f = T[0]

    result = [ 0 ]

    # print_arr(F)
    # print(n)
    while next_i != -1 and F[next_i][next_f] != -1:
        print( F[next_i][next_f])
        result.append( F[next_i][next_f][index] )
        next_i, next_f = F[next_i][next_f][index], F[next_i][next_f][fuel]
        if next_f >= n: 
            break

    # print_arr( F )

    # print( F[ 0 ][ T[0] ] )
    # print( F[ )

    # while next_i != -1 and F[next_i][next_f] != -1:
    #     result.append(next_i)
    #     print( F[next_i][next_f])
    #     if next_f >= n - 1:
    #         next_f = n - 1
    #     next_i, next_f = F[next_i][next_f][index], F[next_i][next_f][fuel]



    # while next_i != -1 and F[next_i][next_f] != -1 and next_f + next_i < n:
    #     print(result)
    #     result.append( next_i )
    #     next_i, next_f = F[next_i][next_i + next_f][index], F[next_i][next_i + next_f][fuel]  



    # tu prosze wpisac wlasna implementacje
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )