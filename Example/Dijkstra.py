#coding=utf-8
'''
Dijkstr(迪杰斯特拉)算法，用于求图中指定两点之间的最短路径，或者是指定一点到其它所有点之间的最短路径
'''

def dijkstra(graph, startIndex, path, cost, max):
    '''
    求解各节点最短路径，获取path，和cost数组，
    path[i] 表示vi节点的前继节点索引，一直追溯到起点。
    cost[i] 表示vi节点的花费
    '''
    lenth = len(graph)
    v = [0] * lenth
    # 初始化 path，cost，V
    for i in range(lenth):
        if i == startIndex:
            v[startIndex] = 1
        else:
            cost[i] = graph[startIndex][i]
            path[i] = (startIndex if (cost[i] < max) else -1)
    for i in range(1, lenth):
        minCost = max
        curNode = -1
        for w in range(lenth):
            if v[w] == 0 and cost[w] < minCost:
                minCost = cost[w]
                curNode = w
        if curNode == -1: break
        # 剩下都是不可通行的节点，跳出循环
        v[curNode] = 1
        for w in range(lenth):
            if v[w] == 0 and (graph[curNode][w] + cost[curNode] < cost[w]):
                cost[w] = graph[curNode][w] + cost[curNode] # 更新权值
                path[w] = curNode # 更新路径
    return path,cost

if __name__ == '__main__':
    max = 9999999
    graph = [
        [max, max, 10, max, 30, 100],
        [max, max, 5, max, max, max],
        [max, max, max, 50, max, max],
        [max, max, max, max, max, 10],
        [max, max, max, 20, max, 60],
        [max, max, max, max, max, max],
        ]
    path = [0] * 6
    cost = [0] * 6
    path,cost = dijkstra(graph, 0, path, cost, max)
    print('0节点到其他节点最短路径前继节点： '+ str(path))
    print('0节点到其他节点最短路径权重： ' + str(cost))