class TrieNode:
    def init(self):
        self.childs = {}
        self.is_end = False
        self.word_idxes = []

class Trie:
    def init(self):
        self.root = TrieNode()
    def get_root(self):
        return self.root

    def insert(self, string, index):
        curr = self.get_root()
        for ch in string:
            if curr.childs.get(ch) == None:
                new_node = TrieNode()
                curr.childs[ch] = new_node
            curr = curr.childs[ch]
            if len(curr.word_idxes) < 5:
                curr.word_idxes.append(index)
        curr.is_end = True

    def getPrefixNode(self, prefix):
        curr = self.get_root()
        for i in range(len(prefix)):
            ch = prefix[i]
            if curr.childs.get(ch) == None:
                return []
            curr = curr.childs[ch]
        return curr.word_idxes

def solve(A, B, Q):
    trie = Trie()
    words = [(A[i], B[i]) for i in range(len(A))]
    words.sort(key = lambda x: x[1], reverse=True)

    for i in range(len(words)):
        word = words[i][0]
        trie.insert(word, index=i)
    for pref in Q:
        prefIndexes = trie.getPrefixNode(pref)
        if len(prefIndexes) == 0:
            print(’-1’, end=’ ‘)
        else:
            for idx in prefIndexes:
                print(words[idx][0], end=’ ‘)
        print()

def main():
    tc = int(input())
    for _ in range(tc):
        n, m = input().split(’ ‘)
        A = input().split(’ ‘) # words in dict
        B = list(int(x) for x in input().split(’ ‘)) # word weight
        Q = input().split(’ ') # Queries
        solve(A, B, Q)