class TrieNode:
    def __init__(self, char=None): 
        self.char = char
        self.children = {}
        self.end_node = False;

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
            currentNode = self.root
            for ch in word:
                if currentNode.children.get(ch) == None:
                    currentNode.children[ch] = TrieNode(char=ch)
                currentNode = currentNode.children[ch]
            currentNode.end_node = True


    def search(self, pattern):
        currentNode = self.root
        for ch in pattern:
            if currentNode.children.get(ch) != None:
                    currentNode = currentNode.children[ch]
            else:
                    return False
        return currentNode.end_node