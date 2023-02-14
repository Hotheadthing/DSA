class TrieNode:
    def __init__(self,letter):
        self.letter = letter
        self.children = {}
        self.is_the_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self,word):
        node = self.root
        for d in word:
            if d not in self.children:
                self.children[d] = TrieNode(d)
            node = self.children[d]
        node.is_the_end = True


# def solve(self,A):
A = [1,2,3,4,5]
A = [5, 17, 100, 11]
A = [ 2, 6, 10, 2, 9, 9, 6, 10, 6, 8, 6, 4, 4 ]
val = max(A)
val_bin = bin(val)[2:]
length = len(val_bin)
arr = []
for i in range(len(A)):
    if A[i] != val:
        ans = bin(A[i])[2:]
        # print(ans,A[i])
        va = ""
        if len(ans) < length:
            ins = length - len(ans)
            for i in range(ins):
                va += "0"
            ans = va + ans
            arr.append(ans)
        elif len(ans) == length:
            arr.append(ans)

# print(1^4^3)
# print(6^1)
# print(1^4)
# 63
A = [33, 34, 14, 10, 16, 23, 31, 8, 32]
print(34^14^10^16^23^31^8^32)

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 79 0 0 0 0 0 46 0 0 0 0 0 58 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 17 0 0 0 0 0 93 0 0 0 0 53 0 0 0 56 90 0 0 0 0 0 0 0 0 0 0 0 0 10 0 0 54 0 0 0 46 40 96 0 0 0 0 0 0 0 0 82 0 0 0 0 0 0 0 0 23 44 0 0 0 0 0 0 0 0 0 0 0 10 0 0 69 93 0 75 15 0 59 0 0 12 0 26 0 0 0 99 86 0 0 0 0 31 15 0 0 83 0 27 0 0 0 0 30 0 0 97 4 69 0 46 98 0 0 0 0 0 92 83 65 0 25 0 0 0 59 0 0 0 40 9 0 0 0 0 57 0 40 24 35 90 0 0 0 30 0 0 0 24 0 0 0 62 0 0 0 0 0 37 94 58 80 26 71 0 0 38 0 54 0 62 35 77 16 22 43 0 0 84 36 0 26 7 0 0 96 43 39 83 51 6 99 87 3 0 0 0 41 89 33 85 0 0 86 75 8 34 0 0 88 0 0 0 0 0 97 0 0 72 65 17 41 0 0 93 0 0 47 22 0 31 52 85 67 78 0 0 0 0 99 13 72 0 59 4 92 61 0 27 0 28 28 0 55 69 49 0 0 0 3 74 22 0 97 20 1 0 92 8 45 3 0 98 14 91 73 95 51 49 96 10 86 19 0 30 90 68 82 6 20 28 0 13 71 76 56 92 0 35 73 10 0 44 97 0 10 62 19 0 26 33 24 13 94 0 15 0 88 59 94 6 79 89 12 85 0 74 19 14 77 56 93 54 86 0 8 78 1 42 30 66 25 92 37 87 89 24 1 84 45 60 9 24 0 96 99 89 42 56 47 42 58 51 44 49 2 12 0 92 59 35 45 63 23 76 15 54 63 55 22 96 22 59 38 96 6 67 38 71 54 27 59 94 100 78 75 71 71 3 93 23 29 46 25



