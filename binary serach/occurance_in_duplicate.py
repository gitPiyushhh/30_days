##############################################
#### First occurance

def first_occurrence(arr, key):
    s = 0
    e = len(arr)-1
    f = -1

    while s <= e:
        m = s + (e-s) // 2
        
        if arr[m] < key:
            s = m +1
        
        else:
            if arr[m] == key: f = m
            e = m - 1
        
    return f


##############################################
#### Last occurance

def last_occurrence(arr, key):
    s = 0
    e = len(arr)-1
    l = -1

    while s <= e:
        m = s + (e-s) // 2
        
        if arr[m] > key:
            e = m - 1
        
        else:
            if arr[m] == key: l = m
            s = m + 1
        
    return l

print(first_occurrence([1,2, 2, 2, 3, 5, 7, 9], 2))
print(last_occurrence([1,2, 2, 2, 3, 5, 7, 9], 2))