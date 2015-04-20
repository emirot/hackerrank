

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.node = None


    def add_in_head(self,val):
        new_node = Node(val)
        new_node.next = self.node
        self.node = new_node


    def add_in_tail(self,val):
        tmp = self.node
        while tmp.next != None:
            tmp = tmp.next
        new_node = Node(val)
        tmp.next = new_node


    def traverse_linked(self):
        tmp = self.node
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next



if __name__ == '__main__':
    l = LinkedList()
    l.add_in_head(3)
    l.add_in_head(5)
    l.add_in_tail(4)
    l.traverse_linked()
