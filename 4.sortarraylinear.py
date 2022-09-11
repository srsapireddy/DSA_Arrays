def array(arr):
    start = 0
    idx = 0
    while(idx<5):
        if arr[idx] == 0:
            arr[start],arr[idx] = arr[idx],arr[start]
            start += 1
        idx += 1
    return print(arr)

arr = [1,1,0,1,0]
array(arr)