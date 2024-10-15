# 小红在第三新北林市的学园城送外卖，学园城中有非常多的学校，学园城里有一个美食街。小红每次会接一些同一个学校的订单，然后从美食街取餐出发，再骑车将外卖送到学校，最后回到美食街，以此往复。
# 学园城有 
# n
# n 个结点， 
# m
# m 条道路，美食街为1号结点，剩下的结点都是学校，保证学园城中所有结点连通。给出小红每次要送外卖的学校，请计算小红最少需要骑行的距离。

import heapq
class Node:
    def __init__(self, node,weight):
        self.node = node
        self.weight = weight

    def __lt__(self, other):
        return self.weight< other.weight

n,m,q=map(int,input().split())
graph=[[] for _ in range(0,n+1)]
visited=[0 for _ in range(0,n+1)]
dist=[float('inf') for _ in range(0,n+1)]
for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append(Node(v,w))
    graph[v].append(Node(u,w))
alls=list(map(int,input().split()))
sum=0
for i in range(q):
    a=alls[i]
    dist[1]=0
    heap=[]
    heapq.heappush(heap,Node(1,0))
    while(len(heap)!=0):
        node=heapq.heappop(heap)
        for i in graph[node.node]:
            if dist[i.node]>dist[node.node]+i.weight:
                dist[i.node]=dist[node.node]+i.weight
                heapq.heappush(heap,Node(i.node,dist[i.node]))
    sum+=2*dist[a]
print(sum) 
    


