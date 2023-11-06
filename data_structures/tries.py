
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_word: bool = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()

            currentNode = currentNode.children[char]
        
        currentNode.is_word = True

    def search(self, word: str) -> bool:
        search_results = self._search(word)
        return search_results and search_results.is_word

    def starts_with(self, prefix: str) -> bool:
        return bool(self._search(prefix))
    
    def _search(self, word: str):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return None
            
            currentNode = currentNode.children[char]

        return currentNode

if __name__ == '__main__':
    pass 