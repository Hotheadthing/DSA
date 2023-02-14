if C[-1] <= B:
    y.append(C[-1])
elif B == 1 and C[0] <= B:
    y.append(C[0])
elif B ==1 and C[0] > B:
    y.append(0)
else:
    for i in range(A):
        if i == 0 and C[i] > B:
            y.append(i)
            break
        elif i == 0 and C[i] == B:
            y.append(B)
            break