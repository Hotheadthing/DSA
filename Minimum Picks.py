A = [5,17,100,1]
Even = []
Odd = []

for elements in A:
    if elements % 2 == 0:
        Even.append(elements)
    else:
        Odd.append(elements)

Even.sort()
Odd.sort()

Result = Even[-1] - Odd[0]
print(Result)