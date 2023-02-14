# A = "aab"
A = "bcbc"
A = "vleirzohviwfaqnefbdwzpcjdlxhqollqfdrdqvhqlinlggbmpxqwfsdytuihbmkssmelzpn"
# A = "fnmzxvozgkpkwuuwbnlbajogijoaxipjwwfaqefjnvfbcilerkdaeysamehgdouvspojtuvh"
count = 0
for i in range(len(A)):
    if A[i] == "a":
        count += 1
ans = (count*(count+1))//2
print(ans)
