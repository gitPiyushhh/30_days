def gcd(n1, n2):
    r = min(n1, n2)
    res = 1

    for i in range(1, r+1):
        if n1 % i == 0 and n2 % i == 0: res = i
    
    return res

print(gcd(8, 64))