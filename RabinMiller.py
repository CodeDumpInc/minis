''' Rabin-Miller prime number test'''

'''things learned: python's pow() implements square & multiply :)'''

import random



def rm(n,k):
    if( n < 2 ):
        return False    
    if( n == 2 or n == 3):
        return True

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(0,k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(s-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                continue
        return False
    return True

def getPrime(numBits, k):
    found = False
    
    while not found:
        possP = random.getrandbits(numBits)    
        possP |= 2**(numBits-1)
        possP |= 1
       
        found = rm(possP,k)
        
    return possP

def main():
    numBits = 256
    k = 5
    
    p = getPrime(numBits, k)
    print(p)

if __name__ == "__main__":
   main()



