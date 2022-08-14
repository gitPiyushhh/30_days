def floor(arr, key):
    s = 0
    e = len(arr)-1
    f = -1

    while s <= e:
        m = s + (e-s) // 2

        if arr[m] == key:
            return m
        
        if arr[m] < key:
            f = m
            s = m +1
        
        else:
            e = m - 1
        
    return f

print(floor([1, 2, 3, 5, 7, 9], 1))