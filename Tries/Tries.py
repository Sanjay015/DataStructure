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

    def search(self, word):
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

    def _walk(self, node, word, word_list):
        if node.children:
            for element in node.children:
                new_word = word + element
                if node.children[element].is_end_of_word:
                    word_list.append(new_word)
                self._walk(node.children[element], new_word, word_list)

    def auto_complete(self, partial_word):
        current_node = self.root
        words_list = []
        for word in partial_word:
            if word in current_node.children:
                current_node = current_node.children[word]
            else:
                return words_list

        if current_node.is_end_of_word:
            words_list.append(partial_word)

        self._walk(current_node, partial_word, words_list)
        return words_list


if __name__ == '__main__':
    trie = Trie()
    words = ['wait', 'waiter', 'shop', 'shopper']
    trie.add_word('wait')
    trie.add_word('waiter')
    trie.add_word('shop')
    trie.add_word('shopper')
