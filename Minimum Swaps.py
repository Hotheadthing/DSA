A = [1, 12, 10, 3, 14, 10, 5]
B = 8
A = [ 52, 7, 93, 47, 68, 26, 51, 44, 5, 41, 88, 19, 78, 38, 17, 13, 24, 74, 92, 5, 84, 27, 48, 49, 37, 59, 3, 56, 79, 26, 55, 60, 16, 83, 63, 40, 55, 9, 96, 29, 7, 22, 27, 74, 78, 38, 11, 65, 29, 52, 36, 21, 94, 46, 52, 47, 87, 33, 87, 70 ]
B = 19
# A = [5, 17, 100, 11]
# B = 20
# A = [ 31, 98, 58, 86, 36, 31, 3, 22, 4, 17, 51, 33, 56, 7, 91, 17, 59, 66, 54, 67, 55, 41, 58, 24, 100, 1, 98, 68, 21, 33, 27, 67, 20, 66, 20, 100, 36, 89, 20, 15, 13, 26, 11, 29, 99, 36, 39, 49, 74, 77, 54, 66, 30, 21, 14, 18, 83, 72, 10, 22, 53, 83, 60, 9, 68, 56, 9, 21, 77, 44, 45, 61, 97, 82, 35, 16, 38, 95, 55, 11, 46, 77, 25, 3, 44 ]
# B = 18

count = 0
for i in range(len(A)):
    if A[i] <= B:
        count += 1
# print(f"the value of count is {count}")

larger = 0
for i in range(count):
    if A[i] > B:
        larger += 1
# print(f"the value of larger is {larger}")

ans = larger
j = count
for i in range(len(A)):
    if j == len(A):
        break

    if A[i] > B:
        larger = larger - 1

    if A[j] > B:
        larger = larger + 1
        # print(f"the value of A[j] is {A[j]}")

    # print(f"The value of min(ans,larger) is {ans},{larger}")
    ans = min(ans,larger)

    j = j + 1
print(ans)