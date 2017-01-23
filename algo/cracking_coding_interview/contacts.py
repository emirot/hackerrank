

class Node:

    def __init__(self):
        self.children = {}
        self.is_leaf = False
        self.count_ = 0


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def add(self, word):
        current_node = self.root
        for c in word:
            if c in current_node.children:
                current_node = current_node.children[c]
                current_node.count_ += 1
            else:
                current_node.children[c] = Node()
                current_node = current_node.children[c]
                current_node.count_ += 1
        current_node.is_leaf = True

    def __contains__(self, item):
        pass

    def auto_complete(self, word):
        current_node = self.root
        prefix_w = ""
        words = []
        try:
            for c in word:
                current_node = current_node.children[c]
                prefix_w += c
        except KeyError:
            return 0

        return current_node.count_



if __name__ == '__main__':
    p = PrefixTree()
    n = int(raw_input().strip())
    for a0 in xrange(n):
        op, contact = raw_input().strip().split(' ')
        if op == 'add':
            p.add(contact)
        if op == 'find':
            r = p.auto_complete(contact)
            print(r)

