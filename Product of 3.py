import heapq

A = [1, 2, 3, 4, 5]
# A = [10, 2, 13, 4]
# A = [ 11, 5, 6, 2, 8, 10 ]

heap_arr = []
arr = []
curr_product = 1


for i in range(3):
    if i < 2:
        arr.append(-1)
        curr_product = curr_product * A[i]
        heap_arr.append(A[i])
    else:
        curr_product = curr_product * A[i]
        arr.append(curr_product)
        heap_arr.append(A[i])

heapq.heapify(heap_arr)
curr_product = 1

for i in range(3,len(A)):
    heapq.heappush(heap_arr, A[i])
    val_removed = heapq.heappop(heap_arr)
    product = arr[-1]
    if val_removed == A[i]:
        new_product = arr[-1]
    else:
        new_product = (product//val_removed) * A[i]
    arr.append(new_product)

print(arr)



# print(heap_arr)
# element = heapq.heappop(heap_arr)
# print(element)
# print(f"the value removed = {val_removed}")
# print(f"the product is {product}")
# print(f"the new_product is {new_product}")