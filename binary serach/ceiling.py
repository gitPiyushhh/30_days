def ceiling(arr, key):
    s = 0
    e = len(arr)-1
    ceil = -1

    while s <= e:
        m = s + (e-s) // 2

        if arr[m] == key:
            return m
        
        if arr[m] < key:
            s = m +1
        
        else:
            ceil = m
            e = m - 1
        
    return ceil

print(ceiling([1, 2, 4, 5, 9], 16))