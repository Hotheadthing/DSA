#A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
B = ''.join(A)
if B.isalnum() == True:
    print(1)
else:
    print(0)