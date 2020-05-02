def sortedInsert(head, data):
    tmp = head
    if tmp is None:
        head = DoublyLinkedListNode(data)
        return head
    if data < tmp.data:
        new_node = DoublyLinkedListNode(data)
        tmp.prev = new_node
        new_node.next = tmp
        head = new_node
        return head
    while tmp.next:
        if tmp.next.data > data:
            break
        tmp = tmp.next
    new_node = DoublyLinkedListNode(data)
    new_node.prev = tmp
    new_node.next = tmp.next
    tmp.next = new_node
    return head
