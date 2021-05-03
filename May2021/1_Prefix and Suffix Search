class WordFilter(object):

    def __init__(self, words):
    
        trie = lambda: collections.defaultdict(trie)
        self.trie = trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur["weight"] = weight
                for j in range(i, 2*len(word)-1):
                    cur = cur[word[j%len(word)]]
                    cur["weight"] = weight
                    
    def f(self, prefix, suffix):

        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur["weight"]
