"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    currentA = headA
    currentB = headB
    try:
        while currentA or currentB:
            if currentA.data != currentB.data:
                return 0
            currentA = currentA.next
            currentB = currentB.next
    except:
        return 0
    return 1
