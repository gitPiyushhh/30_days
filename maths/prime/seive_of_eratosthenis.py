def seive(n):
    # 1. Array lo{True se pura}
    arr = [True] * (n+1)

    # 2. Loop chlao {1-7}
    for i in range(2, min(n, 7)):
        if arr[i] == True:
            for j in range(i**2, n, i):
                arr[j] = False

    # 3. Jo prime mile uske saare multiple non prime ho jayege
    print(f'Yeah non prime h {arr}')

    for i in range(len(arr)):
        if arr[i]: print(i, end=' ')

seive(5)