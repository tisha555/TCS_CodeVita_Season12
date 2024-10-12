def mac(arr, temp_arr, left, right):
    if left == right:
        return 0
   
    mid = (left + right) // 2
    inv_c = 0
   
    inv_c += mac(arr, temp_arr, left, mid)
    inv_c += mac(arr, temp_arr, mid + 1, right)
   
    inv_c += merge(arr, temp_arr, left, mid, right)
   
    return inv_c

def merge(arr, temp_arr, left, mid, right):
    i = left   
    j = mid + 1 
    k = left   
    inv_c = 0
   
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_c += (mid - i + 1) 
            j += 1
        k += 1
   
   
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
   
   
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
   
    
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
   
    return inv_c

def count_swaps(arr, asc=True):
    n = len(arr)
    temp_arr = [0] * n
   
    if asc:
        return mac(arr, temp_arr, 0, n - 1)
    else:
        arr = arr[::-1]
        return mac(arr, temp_arr, 0, n - 1)


n = int(input())
arr = list(map(int, input().split()))


asc_swaps = count_swaps(arr.copy(), asc=True)
desc_swaps = count_swaps(arr.copy(), asc=False)

print(min(asc_swaps, desc_swaps), end="")
