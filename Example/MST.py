#coding=utf-8
'''
一个有 n 个结点的连通图的生成树是原图的极小连通子图，且包含原图中的所有 n 个结点，并且有保持图连通的最少的边。也就是说，
用原图中有的边，连接n个节点，保证每个节点都被连接，且使用的边的数目最少。
例如：要在n个城市之间铺设光缆，主要目标是要使这 n 个城市的任意两个之间都可以通信，但铺设光缆的费用很高，且各个城市之间
铺设光缆的费用不同，因此另一个目标是要使铺设光缆的总费用最低。这就需要找到带权的最小生成树。
'''

class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()

    def get_nodenum(self):
        return len(self.maps)

    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
                    count += 1
        return count

    def kruskal(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        edge_list = []
        for i in range(self.nodenum):
            for j in range(i, self.nodenum):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])  # 按[begin, end, weight]形式加入
        edge_list.sort(key=lambda a: a[2])  # 已经排好序的边集合
        group = [[i] for i in range(self.nodenum)]
        for edge in edge_list:
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                res.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return res

    def prim(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        res = []
        seleted_node = [0]
        candidate_node = [i for i in range(1, self.nodenum)]
        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999
            for i in seleted_node:
                for j in candidate_node:
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            res.append([begin, end, minweight])
            seleted_node.append(end)
            candidate_node.remove(end)
        return res


max_value = 9999    ##未直接相连就将边的权重设为最大
row0 = [0, 7, max_value, max_value, max_value, 5]
row1 = [7, 0, 9, max_value, 3, max_value]
row2 = [max_value, 9, 0, 6, max_value, max_value]
row3 = [max_value, max_value, 6, 0, 8, 10]
row4 = [max_value, 3, max_value, 8, 0, 4]
row5 = [5, max_value, max_value, 10, 4, 0]
maps = [row0, row1, row2, row3, row4, row5]
graph = Graph(maps)
print('邻接矩阵为： \n' +  '\n'.join(list(map(str,graph.maps))))
print('共有%d个节点，%d条边\n' % (graph.nodenum, graph.edgenum))
print('------最小生成树kruskal算法------')
print(graph.kruskal())
print('--------最小生成树prim算法-------')
print(graph.prim())
