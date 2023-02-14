A = "x^y/(a*z)+b"
A = "a+b*(c^d-e)^(f+g*h)-i"
A = "l-(l*q/s)/q*(u-p)"
stack = []
string = ""
hmap = {"^": 3, "/": 2, "*": 2, "+": 1, "-": 1, "(": 0, ")": 0}

for i in range(len(A)):
    if A[i] not in hmap:
        string += A[i]
    else:
        if A[i] == "(":
            stack.append(A[i])
        elif A[i] == ")":
            while stack[-1] != "(":
                string += stack[-1]
                stack.pop()
            stack.pop()
        else:
            if len(stack) == 0:
                stack.append(A[i])
            else:
                if hmap[stack[-1]] >= hmap[A[i]]:
                    while hmap[stack[-1]] >= hmap[A[i]]:
                        string += stack[-1]
                        stack.pop()
                        if len(stack) == 0:
                            break
                    stack.append(A[i])
                else:
                    stack.append(A[i])

print(string)
print(stack)
for i in range(len(stack)-1,-1,-1):
    string += stack[i]

print(string)



