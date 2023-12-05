Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 
Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

class Trie:

    def __init__(self):
        self.words = {}

    def insert(self, word: str) -> None:
        current = self.words
        for char in word:
            if char not in current:
                # nested dictionaries
                current[char] = {}
            current = current[char]

        # termination symbol, we have this only at the end of a word
        current['*'] = None

    def search(self, word: str) -> bool:
        # Not used in this task
        current = self.words
        for char in word:
            if char not in current:
                return False
            current = current[char]

        return '*' in current

    def startsWith(self, prefix: str) -> bool:
        # Not used in this task
        current = self.words
        for char in prefix:
            if char not in current:
                return False
            current = current[char]

        return True


class WordDictionary:

    def __init__(self):
        # Local trie object
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        # delegate insert logic to the trie
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        # Call the helper function
        return self._search(0, word, self.trie.words)

    def _search(self, current_idx, word, trie_dict):
        # current_idx: Current index in the search request word
        # word: search request word
        # trie_dict: current level

        if current_idx == len(word):
            # No more chars, we check if this node has a termination of a word
            return '*' in trie_dict

        char = word[current_idx]
        if char not in trie_dict and char != '.':
            # No wildcard match and the current character isn't in the Trie
            return False

        if char == '.':
            # Wildcard match means that we check in all child dictionaries
            for d in trie_dict:
                # No need to check termination characters
                if d != '*' and self._search(current_idx + 1, word, trie_dict[d]):
                    return True

            return False

        if char in trie_dict:
            # Exact match found, we check the next one
            return self._search(current_idx + 1, word, trie_dict[char])

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
