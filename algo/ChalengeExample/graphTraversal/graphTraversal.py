a__author__ = 'nolanemirot'


def iterativeDfs(graph, start):
    tranversed = []
    stack=[start]
    while stack:
        v = stack.pop()
        if v not in tranversed:
            tranversed.append(v)
            print(v,len(graph[v]))
            stack += graph[v]
            print(v,':',stack)
    return tranversed

if __name__ == '__main__':
    graph = {'A':['B','C','F'],'B':['A','C'],'C':['A','B'],'F':['G','A'],'G':['F']}
    a = iterativeDfs(graph, 'A')
    print(a)