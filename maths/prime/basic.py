import math

def prime(n):
    r = int(math.sqrt(n))
    for i in range(2, r):
        if n % i == 0: return False
    
    return True

print(prime(2))