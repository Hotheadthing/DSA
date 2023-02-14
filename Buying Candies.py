A = [1, 2, 3]
B = [2, 2, 10]
C = [2, 3, 9]
D = 8
A = [2]
B = [5]
C = [10]
D = 99
def unbounded(W,wt,val,quant,n):
    K = [0 for i in range(W+1)]

    for i in range(W+1):
        for j in range(n):
            if wt[j] <= i:
                K[i] = max(K[i],K[i - wt[j]] + (val[j]*quant[j]))
    print(K)

print(unbounded(D,C,B,A,len(C)))