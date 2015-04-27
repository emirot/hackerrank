/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int GetNode(Node *head,int positionFromTail)
{
  int listSize = 0;
  Node *tmp = head;
  while(tmp != NULL){
        
    listSize += 1;        
    tmp = tmp->next;
    // std::cout << "len" << listSize << std::endl;
  }
  Node *tmp2 = head;
  int i=0;
  int val = 0;
  while(i < (listSize  - positionFromTail ) ){
    val =  tmp2->data;
    tmp2 = tmp2->next;
    i +=1;
         
    //std::cout << "val" << tmp2->data << std::endl;
  }
    
  return val;
}
