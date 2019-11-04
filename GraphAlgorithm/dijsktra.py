import time

Matrix = [[0, 2, 5, 1, 999, 999],
           [2, 0, 3, 2, 999, 999],
           [5, 3, 0, 3, 1, 5],
           [1, 2, 3, 0, 1, 999],
           [999, 999, 1, 1, 0, 2],
           [999, 999, 5, 999, 2, 0]]


def dijsktra(Graph):
    Matrix = Graph
    rMatrix = Matrix[:]
    distantDic = dict(zip(range(len(Matrix)), Matrix[0][:]))
    result = [-1]*len(Matrix)

    for j in range(len(Matrix)):
        currentNode,currentDistant = min(distantDic.items(),key=lambda x:x[1])
        print(currentNode,currentDistant)
        result[currentNode] = currentDistant

        for i in range(len(Matrix)):
            if rMatrix[currentNode][i]+currentDistant < rMatrix[0][i]:
                rMatrix[0][i] = rMatrix[currentNode][i]+currentDistant
                distantDic[i] = rMatrix[currentNode][i]+currentDistant
        print("update:",rMatrix[0])

        del distantDic[currentNode]
        print("delete:", distantDic)
    print("\nresult:",result)
    return result

s = time.time()
dijsktra(Matrix)
e = time.time()
print((e-s)*1000,'ms')
