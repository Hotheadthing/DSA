def sort(arr,left,right):
    if left == right:
        return 0
    mid = (left+right) // 2
    A = sort(arr,left,mid)
    B = sort(arr,mid+1,right)
    C = inv_count(arr,left,mid,right)
    merge(arr,left,mid,right)

    count = A + B + C
    return count

def inv_count(arr,left,mid,right):
    i = left
    j = mid + 1
    count = 0
    while i <= mid and j <= right:
        if arr[i] > arr[j] * 2:
            count += mid - i + 1
            j += 1
        else:
            i += 1
    return count
def merge(arr,left,mid,right):
    i = left
    j = mid + 1
    k = 0
    temp_arr = [0] * (right-left+1)

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            temp_arr[k] = arr[j]
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

    counter = 0
    for i in range(left,right+1):
        arr[i] = temp_arr[counter]
        counter += 1

A = [1, 3, 2, 3, 1]
n = len(A)
result = sort(A,0,n-1)
print(result)
