
/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
 */
 /* struct Node
  {
     int data;
     struct Node *next;
  }
  */

Node* Insert(Node *head, int data)
{
   Node *newNode =  (Node*) malloc(sizeof (struct Node));
  newNode->next = NULL;
  newNode->data = data;
  if (head != NULL){

  Node *tmp = head;

  while(tmp->next != NULL){
      tmp = tmp->next;
  }

 tmp->next = newNode;

  return head;
  }
      newNode->next = NULL;
  newNode->data = data;
return newNode;

}
