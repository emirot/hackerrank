"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    tmp = head
    tmp_2 = head
    while tmp is not None and tmp_2.next is not None:
        tmp = tmp.next
        tmp_2 = tmp_2.next.next
        if tmp == tmp_2:
            return True
        
    return False
        
    
