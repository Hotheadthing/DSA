A = 6816621
B = 8157697

if A % B == 0 or B % A == 0:
    print(min(A,B))
elif A > B:
    print(A-B)
elif B > A:
    print(B-A)

# print(A%1341076)
# print(B%1341076)