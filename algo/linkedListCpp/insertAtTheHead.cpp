
Node* Insert(Node *head,int data)
{
  Node *newNode =  (Node*) malloc(sizeof (struct Node));
  newNode->data = data;
  newNode->next = head;
  head  = newNode;
  return head;
}
