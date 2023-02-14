A = [1]
Even = []
Odd = []

for digit in A:
    if digit % 2 != 0:
        Odd.append(digit)
if len(Odd) % 2 != 0:
    print("No")
else:
    print("Yes")

# print(5^1)

print(4^3)