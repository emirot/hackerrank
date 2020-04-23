""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def is_binary_search_tree(root,  min_val, max_val):
    if not root:
        return True
    if root.data <= min_val or root.data >= max_val :
        return False
    return is_binary_search_tree(root.left, min_val, root.data ) and is_binary_search_tree(root.right, root.data , max_val)


def check_binary_search_tree_(root):
    
    return is_binary_search_tree(root, float('-inf'), float('inf'))

    
    

    
    
    
    
