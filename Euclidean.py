'''Euclidean Algorithm to compute the GCD of two numbers

        gcd(24, 74):
        a   |     b  |    h  
        24 |    74 |    -
        --------------------   h = a%b, a = b, b = h
        74 |  24 |  24      (b>a - numbers are swapped)
        24 |    2 |    2
          2 |    2 |    0
'''

def printExtenedEuclidResult(res):
    print("gcd (" + str(res['a']) + ", " + str(res['b']) + ") = " + str(res['gcd']) + ".")
    if(res['inv']):
        print(str(res['b']) + "^-1 mod " + str(res['a']) + " = " + str(res['inv']) + ".")
    print()

def euclid(a,b):
    while b != 0:   
        h = a % b
        a = b
        b = h
    return a

def extendedEuclid(a,b):
    s1 = 1
    s2 = 0
    s3 = 0
    s4 = 1
    
    res = {'a':a, 'b':b, 'inv':None}

    #swap to keep structure
    if( a < b):
        a,b = b,a

    while b != 0:
        tmp  = a % b
        factor = int(a / b)

        #compute next u,v and assign them
        s1, s3 = s3, s1 - s3 * factor
        s2, s4 = s4, s2 - s4 * factor
       
        a = b
        b = tmp

        #if there's a inverse, store it
        if b == 1:
            res['inv'] = s4

    res.update({'gcd':a, 'u': s3, 'v': s4})
             
    return res

print(euclid(35,14))

res = extendedEuclid(35, 14)

printExtenedEuclidResult(res)

res = extendedEuclid(11, 3)

printExtenedEuclidResult(res)
