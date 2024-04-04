

def get_out(arr:list) -> int:
    n = 0
    j = 0
    while n < len(arr):
        j += 1
        v = arr[n]
        n += v
        #print(f'Jump: {j}, frog at position {n} ({v})')
        #j += 1
        if j > 2+len(arr):
            return -1

    return j

print(get_out([1, 2, 2, -1]))
print(get_out([1, 2, 1, 5]))
print(get_out([1, -1]))
print(get_out([2, -1, 2, -1]))
