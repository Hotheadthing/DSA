A = [1, 2]
# A = [1, 5, 2, 1]
l_r = [1] * len(A)
r_l = [1] * len(A)
for i in range(1,len(A)):
    if A[i] > A[i-1]:
        l_r[i] = l_r[i-1] + 1
print(l_r)

for j in range(len(A)-2,-1,-1):
    if A[j] > A[j+1]:
        r_l[j] = r_l[j+1] + 1

print(r_l)

distribution = []

for k in range(len(l_r)):
    candy = max(l_r[k],r_l[k])
    distribution.append(candy)

print(distribution)

total_candies = 0
for candy in distribution:
    total_candies += candy

print(total_candies)