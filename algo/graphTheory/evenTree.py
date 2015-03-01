__author__ = 'nolanemirot'




def traverseGraph(graph, start):
    traversed = []
    a = 0
    stack = [start]
    first = []
    while stack:
        v = stack.pop()
        if v not in traversed:
            traversed.append(v)
            if v in graph:
                stack += graph[v]
                if start == 1:
                    first = graph[v]
                if v != start and len(graph[v])+1 % 2 == 0:
                    print("v",v)
                    a += 1
                    #print("v:",v,len(graph[v]))
    print(a)




if __name__ == '__main__':
    dic = {}
    firstLine = input()
    l = list(map(int, firstLine.split()))
    nbEdge = l[1]
    i = 0
    while i < nbEdge:
        line  =  input()
        l = list(map(int, line.split()))
        if l[1] in dic:
            dic[l[1]].append(l[0])
        else:
            dic[l[1]] = [l[0]]
            print(dic)
        i += 1
        res = 0

    #print(dic)
    traverseGraph(dic, 1)