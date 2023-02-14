A = 3
A_bin = bin(A)[2:]
print(A_bin)
magic_number = 0
count = 0

for i in range(len(A_bin)-1,-1,-1):
    magic_number += int(A_bin[i]) * 5 ** ((len(A_bin)) - i)
    # if i == (len(A_bin) -1):
    #     magic_number += int(A_bin[i]) * 5
    #     # print(f"for 0th index {magic_number}")
    # elif i == 0:
    #     magic_number += 5**(len(A_bin))
    #     # print(f"for msb index {magic_number}")
    # else:
    #     magic_number += int(A_bin[i]) * 5**((len(A_bin)) - i)
    #     # print(f"for other indexes {magic_number}")
print(magic_number)




