
/*
  Detect loop in a linked list
  List could be empty also
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
#include <set>
int HasCycle(Node* head)
{
   std::set<int*> myset;
   Node *tmp = head;
   while (tmp != NULL){
       if (myset.count(&tmp->data) > 0){
           return 1;
       }
       myset.insert(&tmp->data);
       tmp = tmp->next;
   }
    return 0;
}
