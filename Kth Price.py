A = [2, 1, 4, 3, 2]
k = 3


def count(arr,mid):
    count = 0
    for i in range(len(arr)):
        if arr[i] <= mid:
            count += 1
    return count


minimum = min(A)
maximum = max(A)

while minimum < maximum:
    print(minimum,maximum)
    mid = (minimum + maximum)//2
    print(mid)
    if count(A,mid) < k:
        minimum = mid + 1
    else:
        maximum = mid
# print(minimum)

