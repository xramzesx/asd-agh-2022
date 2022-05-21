# zad7testy.py
from testy import *
from zad7test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( G):
    print("G : ", limit(G))


def printhint( hint ):
    print("Mozliwe wyniki  : ", limit(hint) )


def printsol( sol ):
    print("Otrzymany wynik : ", limit(sol) )

# def check( G, hint, sol ):
#   if hint==None : 
#     return hint==sol
#   else:
#     if str(type(sol))!="<class 'list'>": return False
#     if sorted(sol)!=[i for i in range(len(G))]: return False
#     n = len(G)
#     for i in range(1,n):
#       if sol[i-1] not in G[ sol[i] ][ 0 ] + G[sol[i]][ 1 ]: return False

#     if sol[n-1] not in G[sol[0]][0]+G[sol[0]][1]: return False
#     return True
    
def check( G, hint, sol ):
    if sol is None:
        if hint == '*':
            print("Ze studenckiej wiedzy wynika, że istnieje rozwiązanie != None")
            return False
        else: return hint == sol
    else:
        if str(type(sol)) != "<class 'list'>": return False
        if sorted(sol) != [i for i in range(len(G))]: return False
        n = len(G)
        if n < 2: return False
        if sol[1] in G[sol[0]][0]: gate = 0
        elif sol[1] in G[sol[0]][1]: gate = 1
        else: return False
        for i in range(n-1):
            if sol[i+1] in G[sol[i]][gate]:
                if sol[i] in G[sol[i+1]][0]: gate = 1
                else: gate = 0
            else: return False
        if sol[0] not in G[sol[n-1]][gate]: return False
    return True


def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)
              
    return TESTS


 
def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

