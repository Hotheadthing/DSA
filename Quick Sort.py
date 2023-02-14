A = [1, 4, 10, 2, 1, 5]

def sort(arr,left,right):
    if left < right:
        index = quick_sort(arr, left, right)
        sort(arr, left, index-1)
        sort(arr, index+1, right)


def quick_sort(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left,right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i + 1

print(A)
n = len(A)
x = sort(A, 0, n-1)
print(A)
