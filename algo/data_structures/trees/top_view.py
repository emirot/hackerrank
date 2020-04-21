def topView(root):
    #Write your code here
    if not root:
        return 
    queue = [[root, 0, 0]]
    res = [[root.info, 0, 0]]
    while queue:
        node, depth, x = queue.pop(0)
        if node.left:
            res.append([node.left.info, depth + 1, x - 1])
            queue.append([node.left, depth+1, x - 1])
        if node.right:
            res.append([node.right.info, depth+1, x+1])
            queue.append([node.right, depth+1, x+1])
    taken = set()
    r = []
    
    for v, y, x in sorted(res,  key=lambda x: (x[2], x[1])):
        if x not in taken:
            r.append(v)
            taken.add(x)
    print(" ".join([str(e) for e in r]))
