__author__ = 'nolanemirot'

import queue;

mygraph = {
    "a" : ["c"],
    "b" : ["c","e"],
    "c" : ["a","b","d","e"],
    "d" : ["c"],
    "e" : ["c","b"],
    "f" : []
}


def generate_edges():
    edg = []
    for node in mygraph:
        for e in mygraph[node]:
            edg.append((e,node))
    return edg

def parcours_graph():
    arr = []
    arr.insert(0,"a")
    arr.insert(0,"b")


def createGraph():
    print(mygraph)


if __name__ == '__main__':
    a = []
    a.append("dsad")
    a.append("nolan")
    a.append("doubi")
    print(a.pop())
    # createGraph()
    #edges = generate_edges()
    #print(edges)
    parcours_graph()