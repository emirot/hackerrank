
/*
  Print elements of a linked list in reverse order as standard output
  head pointer could be NULL as well for empty list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
#include <iostream>
#include <stack>
void ReversePrint(Node *head)
{
  std::stack<int> mystack;
  Node *tmp = head;
  while (tmp != NULL){
      mystack.push(tmp->data);
      tmp =  tmp->next;
  }
  while (!mystack.empty())
  {
     std::cout << mystack.top() << std::endl;
     mystack.pop();
  }

}
