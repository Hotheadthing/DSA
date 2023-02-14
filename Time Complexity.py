# a = 0
# b = 0
# N = 6
# for i in range(N):
#     for j in range(N):
#         a = a + j
#         # print(a)
# for k in range(N):
#     b = b + k
#     print(b)


# TC- O(N) -Expected (TBC)
# *******************************************************************
# count = 0
# N = 6
# i = N
# while i>0:
#     for j in range(i):
#         count += 1
#         # print(count)
#     i = i // 2
#     print(i)
# ********************************************************************

# TC-O(N^2) -Expected (C)
# *******************************************************************
# a = 0
# N = 6
# for i in range(N):
#     for j in range(N):
#         a = a + i + j

# TC-O-Expected (C)
# *******************************************************************
# n = 30
# n = n//3
# print(n)
# for i in range(3, n//3, 3):
#     print(f"The value of i is {i}")
#     for j in range(2, n//2, 2):
#         print(j)
        # //O(1) opertion

# TC-O(N^2)-Expected (confusion)
# *******************************************************************
# a= 0
# n = 27
# for i in range(3, n//3, 3):
#     print(i)
#     for j in range(2, n//2, 2):
#         print(f"the value of j is {j}")
#         a += 1

# TC-O(N^2)-Expected (C)
# *******************************************************************
# def solve():
#     i = 1
#     while (i < n):
#         x = i
#         while (x > 0):
#             #O(1) operation
#             x -= 1
#         i += 1


# TC-O(N^2)-Expected (C)
# *******************************************************************
# i = 0
# N = 6
# while i*i <= N:
#     for j in range(N+1):
#         for k in range(N+1):
#             i += 1
#             # O(1) operation
#
#     i += 1

# TC-Code will run indefinitely-Expected (C)
# *******************************************************************
# ans = 0
# for i in range(n):
#     j = i-1
#     while(j >= 0):
#         ans += i + j
#         j += 1


# TC-O(N)(C)
# *******************************************************************
# N = 6
# for i in range(N):
#     for j in range(i, N):
#         print(j)
#         break


# TC-O(log(N)) {Base 3} (C)
# *******************************************************************
# count = 0
# N = 6
# while N > 0:
#     count += 1
#     N = N // 3

# TC-O(4^N) (C)
# *******************************************************************
# N = 6
# def solve(N):
#     for i in range(2 ** N):
#         j = i
#         while j > 0:
#             j -= 1

# TC-O(N^1/2) (C)
# *******************************************************************
# def fun():
#     i = 1
#     n = 16
#     while(i * i <= n):
#         j = 1
#         print(1)
#         while(j * j <= i):
#             # O(1) operation
#             j += i
#         i += 1
# z = fun()
# print(z)