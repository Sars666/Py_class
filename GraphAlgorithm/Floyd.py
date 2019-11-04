Graph = [[0, 999, 999, 1.2, 9.2, 999, 0.5],
         [999, 0, 999, 5, 999, 3.1, 2],
         [999, 999, 0, 999, 999, 4, 1.5],
         [1.2, 5, 999, 0, 6.7, 999, 999],
         [9.2, 999, 999, 6.7, 0, 15.6, 999],
         [999, 3.1, 4, 999, 15.6, 0, 999],
         [0.5, 2, 1.5, 999, 999, 999, 0]]

# 生成路由矩阵
routeMatrix = [[0 for i in range(len(Graph))] for j in range(len(Graph))]
for i in range(len(Graph)):
    for j in range(len(Graph)):
        if (Graph[i][j] > 0) and (Graph[i][j] < 999):
            routeMatrix[i][j] = j + 1
        else:
            routeMatrix[i][j] = 0
print(routeMatrix)

distantMatrix = Graph[:]
for k in range(len(routeMatrix)):
    for i in range(len(routeMatrix)):
        for j in range(len(routeMatrix)):
            if distantMatrix[i][j] > distantMatrix[k][j] + distantMatrix[i][k]:
                distantMatrix[i][j] = distantMatrix[k][j] + distantMatrix[i][k]
                routeMatrix[i][j] = k+1

print(distantMatrix)
print(routeMatrix)
