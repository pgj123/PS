import sys
from collections import deque

sys.setrecursionlimit(100000)
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))


def bfs(x,y):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    queue = deque([[x,y]])
    
    while queue:
        next = queue.popleft()
        for i in range(4):
            nx = next[0] + dx[i]
            ny = next[1] + dy[i]

            # included good
            if nx >= 0 and nx <n and ny>=0 and ny<m:
                if graph[nx][ny] == 1:
                    queue.append([nx,ny])
                    graph[nx][ny] += graph[next[0]][next[1]]
    return graph[n-1][m-1]


#result = bfs(0,0)
#print(result)

def dfs(x,y):
    if x < 0 or x > n or y < 0 or y > m:
        return 0
    

    if(graph[x][y] == 1):
        graph[x-1][y] += dfs(x-1,y)
        graph[x][y-1] += dfs(x,y-1)
        graph[x+1][y] += dfs(x+1,y)
        graph[x][y+1] += dfs(x,y+1)
        return graph[x][y]
    else:
        return 0


result = dfs(0,0)
print(result)