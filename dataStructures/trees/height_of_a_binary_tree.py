def height(root):
    my_stack = []
    my_stack.append(root)
    depth = [1]
    max_ = 0
    while len(my_stack) > 0:
        node = my_stack.pop()
        max_d = depth.pop()
        if max_d > max_:
            max_ = max_d
        if node.left:
            my_stack.append(node.left)
            depth.append(max_d + 1)
        if node.right:
            my_stack.append(node.right)
            depth.append(max_d + 1)
    return max_ -1
