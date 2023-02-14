A = "12"
A = "875361268549483279131"
hmap = {}
hmap.__setitem__(len(A),1)

def dfs(i):
        if i in hmap:
                return hmap[i]

        if A[i] == "0":
                return 0

        res = dfs(i+1)
        if i+1 < len(A) and (A[i] == "1" or A[i] == "2" and A[i + 1] in "0123456"):
                res += dfs(i+2)

        hmap[i] = res
        return res % 1000000007

print((dfs(0)))

