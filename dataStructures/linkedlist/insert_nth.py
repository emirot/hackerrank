"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    tmp = head
    n = Node(data)
    if position == 0:
        n.next = tmp
        head = n
        return head
    else:
        i = 0
        prev_node = head
        tmp = head
        while i < position:
            prev_node = tmp  
            tmp = tmp.next
            i += 1
        prev_node.next = n
        n.next = tmp
        return head
  
  
  
  
  
  
  
  
  
