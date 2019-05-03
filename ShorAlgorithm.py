import numpy as np
from fractions import Fraction
import math
import random

N = int(input("Insert number to be factorized:\n"))

"""
def Shor(N):
    factors=[]
    
    x = random.randint(2,N-1)
    if math.gcd(x,N)!=1:
        #we have at least a factor of N in gcd(x,N), let's go get it!
        return 0
    else:
        n_register=np.zeros()
"""

def obtain_x(Z):
    y=random.randint(2,Z-1)
    while(math.gcd(y,Z)!=1):
        y=random.randint(2,Z-1)
    return y

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


def v_x(x,t,N,two_t):
    xmodn=np.empty((two_t,1))
    xmodn[0]=1
    for j in range(1,two_t):
        xmodn[j]= (x*xmodn[j-1])%N
    return xmodn


def states_measure(z,two_t):
    r=random.randint(0,two_t-1)
    m=z[r]
    indices=np.where(z==m)
    return indices


n,t = size_input(N)

two_t=2**t

print("size of registers n,t:",n,t)

#picking x
x = obtain_x(N)

print("Picked x =%i" % x)

#applying V_x to all registers
modsn=v_x(x,t,N,two_t)

#the resulting states of the first register after measuring the second
result=states_measure(modsn,two_t)




#print("convergents =" ,list_convergents(853,2048))

"""
def continued_fraction(x: list):
    y=[]
    for i in range(len(x)):


def Hadamard

"""