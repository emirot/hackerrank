
/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
    Node *left = NULL;
    Node *current = head;
    Node *right = NULL;
    while (current != NULL){
        right = current->next;
        current->next = left;
        left = current;
        current = right;
    }
   return left;
}
