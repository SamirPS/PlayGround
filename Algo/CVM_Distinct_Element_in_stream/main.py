"""
My implementation of the algorithms that i found here: https://arxiv.org/pdf/2301.10191

"""


from math import log,ceil
from random import random,randint

def Algo_One(A, epsilon, delta):

    p = 1
    X = set()
    numerator = 12* log(8 * len(A) / delta)
    denominator = epsilon ** 2
    thresh = ceil(numerator /denominator)

    for ai in A:

        X.discard(ai)
        if random() < p:
            X.add(ai)
        
        if len(X) == thresh:
            X = {x for x in X if random() >= 0.5}
            p /= 2
            if len(X) == thresh:
                return '⊥'
    
    return len(X) / p

def Algo_Two(A, epsilon, delta):

    p = 1
    X = set()
    numerator = 12* log(8 * len(A) / delta)
    denominator = epsilon ** 2
    thresh = ceil(numerator /denominator)

    for ai in A:

        X.discard(ai)
        if random() < p:
            X.add(ai)
        
        if len(X) == thresh:
            X = {x for x in X if random() >= 0.5}
            p /= 2
    
    return len(X) / p

def GenerateRandomBits(m):
    return [randint(0, 1) for _ in range(m + 1)]

def FirstZeroIndex(array):
    for index, value in enumerate(array):
        if value == 0:
            return index
    return len(array) + 1

def Algo_Three(A):
    m = len(A)
    Y = [set() for _ in range(m+1)]

    for ai in A:
        r = GenerateRandomBits(m+1)
        for k in range(m+1):
            Y[k].discard(ai)
            if k <= FirstZeroIndex(r):
                Y[k].add(ai)
    return Y
