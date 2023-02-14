A = "abba"
B = "cdd"
# A = "acd"
# B = "bay"
A = "tom"
B = "riddle"
string = ""
string = string + A[0]
n = len(A)
l = 1
while l < n:
    if ord(A[l]) <= ord(B[0]):
        print("yes")
        string += A[l]
        l += 1
    else:
        break

string = string + B[0]
print(string)