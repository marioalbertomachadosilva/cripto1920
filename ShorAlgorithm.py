import numpy as np
from fractions import Fraction
import math
import random

#Z = int(input("Insert number to be factorized:\n"))



def Shor(N):
    factors=[]
    n,t = size_input(N)
    x = random.randint(2,N-1)
    if math.gcd(x,N)!=1:
        #we have at least a factor of N in gcd(x,N), let's go get it!
        return 0
    else:
        n_register=np.zeros()


def size_input(x):
    "Determines the dimensions t,n of the initialized state."
    y = math.ceil(math.log(x, 2))
    z = math.ceil(2*math.log(x, 2))
    return y,z



def list_convergents(x,y):
    "Returns the list of all convergents of the fraction x/y"
    z=find_continued_fraction(x,y)
    K=[]
    m=len(z)
    while m!=0:
        K+=[get_continued_fraction(z,m)]
        m-=1
    return K


def find_continued_fraction(x,y,Z=[]):
    "Returns the list of values in the continued fraction of x/y"
    q=y//x
    Z+=[q]
    if y-q*x!=1:
        return find_continued_fraction(y-q*x,x,Z)
    else:
        Z+=[x]
        return Z

def get_continued_fraction(Y,n):
    "Returns the fraction associated with a set Y of values in a continued fraction, using the first n values of Y or all values if n>len(Y)"
    Y=Y[0:n]
    if len(Y)==1:
        return Fraction(1,Y[0])
    else:
        return Fraction(1,Y[0]+get_continued_fraction(Y[1:],n))


print("convergents =" ,list_convergents(853,2048))

"""
def continued_fraction(x: list):
    y=[]
    for i in range(len(x)):


def Hadamard

"""