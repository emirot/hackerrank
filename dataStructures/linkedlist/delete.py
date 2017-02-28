"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    tmp = head
    if head == None:
        return head
    if position == 0:
        head = tmp.next 
        return head
    else:   
        i = 0
        while tmp:
            if i == position:
                prev.next = tmp.next
                return head
            i += 1
            prev = tmp
            tmp = tmp.next
        return head
  
