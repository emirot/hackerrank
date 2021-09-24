#!/bin/python3

def list_len(head):
    i = 0
    tmp = head
    while tmp:
        tmp = tmp.next
        i +=1
    return i

def go_to(head, loc):
    i = 0 
    tmp = head
    while tmp and i < loc:
        tmp = tmp.next
        i += 1
    return tmp.data if tmp else 0

def start_at(head, ct):
    i = 0
    while i < ct:
        head = head.next
        i += 1
    return head

def findMergeNode(head1, head2):
    l1 = list_len(head1)
    l2 = list_len(head2)
    if  l1 > l2:
        diff = l1 - l2
        head1 = start_at(head1, diff)
        while head1 and head2:
            if head1 == head2:
                return head1.data
            head1 = head1.next
            head2 =  head2.next
    elif l2 > l1:
        diff = l2 - l1
        head2 = start_at(head2, diff)
        while head1 and head2:
            if head1 == head2:
                return head1.data
            head1 = head1.next
            head2 =  head2.next
    else:
        while head1 and head2:
            if head1 == head2:
                return head1.data
            head1 = head1.next
            head2 =  head2.next
    
    return None
