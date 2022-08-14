def fact(n):
    ans = 1

    for i in range(n, 0, -1):
        ans *= i
    
    return ans

print(fact(5))