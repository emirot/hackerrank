__author__ = 'nolanemirot'

import math


def rotateMatrix(m):
    layers = math.floor(len(m)/2)
    length =  len(m) -1
    #print(layers)
    #print(length)
    for layer in range(0,layers):

        for i in range(layer,length-layer):
            top = m[layer][i]
            #left to top
            m[layer][i] = m[length-i][layer]

            m[length-i][layer] = m[length-layer][length-i]

            m[length-layer][length-i] = m[i][length-layer]
            m[i][length-layer] = top

    print(m)




if __name__ == '__main__':
    m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    rotateMatrix(m)