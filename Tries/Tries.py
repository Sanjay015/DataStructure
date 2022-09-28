class TrieNode:

    def __init__(self, element):
        self.element = element
        self.children = {}
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode('*')

    def add_word(self, word):
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode(character)
            current_node = current_node.children[character]
        current_node.is_end_of_word = True

    def search(search, word):
        if word == '':
            return True

        current_node = self.root
        for character in word:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        if prefix == '':
            return True

        current_node = self.root
        for element in prefix:
            if element not in current_node:
                return False
            current_node = current_node[element]
        return True


if __name__ == '__main__':
    trie = Trie()
    words = ['wait', 'waiter', 'shop', 'shopper']
    trie.add_word('wait')
    trie.add_word('waiter')
    trie.add_word('shop')
    trie.add_word('shopper')

