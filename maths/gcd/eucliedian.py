def euclidean(n1, n2):
    
    while n1 != n2:
        if n1 > n2: n1 -= n2
        else: n2 -= n1
    
    if n1 == n2: return n1  
        

print(euclidean(3, 4))