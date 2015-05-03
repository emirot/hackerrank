

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

    def recursive_traverse(self, tmp):
        if tmp != None:
            print("val:",tmp.val)
            return self.recursive_traverse(tmp.next)



    def reverse_linked_list(self):
        tmp = self.node
        left = None
        current = tmp
        right = None
        while current != None:
            right = current.next
            current.next = left
            left = current
            current = right
        self.node = left

    def reverse_linked_list_recursion(self, node_old, current):

        if current == None:
            print("new node == None")
            self.node = node_old
            return
        new_node = current.next
        current.next = node_old

        return self.reverse_linked_list_recursion(current, new_node)



    def getHead(self):
        return self.node

    def traverse_linked(self):
        tmp = self.node
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next



if __name__ == '__main__':
    l = LinkedList()
    l.add_in_head(3)
    l.add_in_head(4)
    l.add_in_head(5)
    l.traverse_linked()
    l.reverse_linked_list_recursion(None, l.getHead())
    l.traverse_linked()
