'''Eucledian Algorithm to compute the GCD of two numbers'''

'''
    gcd(24, 74):
        a   |     b  |    h  
        24 |    74 |    -
        --------------------   h = a%b, a = b, b = h
        74 |  24 |  24      (b>a - numbers are swapped)
        24 |    2 |    2
          2 |    2 |    0
'''

def gcd(a,b):
    while b != 0:   
        h = a % b
        a = b
        b = h
        print(a,b,h)
    return a

print( gcd(24, 74))

        
