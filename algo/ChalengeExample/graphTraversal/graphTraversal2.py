__author__ = 'nolanemirot'



def traverse(graph, start):
    traversed = []
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in traversed:
            traversed.append(v)
            for n in graph[v]:
                stack += n
    print(traversed)

if __name__ == '__main__':
    graph = {'A':['B','C'],'B':['F','G'],'F':['A'],'G':[],'C':[]}
    edge = traverse(graph, 'A')