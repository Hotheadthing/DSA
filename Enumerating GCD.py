A = 4
B = 5


def find_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return a % b, b
    else:
        return b % a, a

x = find_gcd(A,B)
print(x)
# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return a strings
#     def solve(self, A, B):
#         A = int(A)
#         B = int(B)
#
#         gcd = find_gcd(A, A + 1)
#         for i in range(A + 2, B + 1):
#             gcd = find_gcd(gcd, i)
#
#         return gcd
#     x = solve("1","3")
#     print(x)