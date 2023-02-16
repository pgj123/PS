n, m, v = map(int,input().split())

data = []
for i in range(n+1):
    data.append([])

visited = [False] * (n+1)

for i in range(m):
    input1, input2 = map(int,input().split())
    data[input1].append(input2)
    data[input2].append(input1)

for i in range(n+1):
    data[i].sort()

result_dfs = []
result_bfs = []

def dfs(node):
    visited[node] = True

    for i in data[node]:
        if not visited[i]:
            visited[i] = True
            result_dfs.append(i)
            dfs(i)

result_dfs.append(v)
dfs(v)

visited = [False] * (n+1)

from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = True

    while(queue):
        next = queue.popleft()
        for i in data[next]:
            if not visited[i]:
                visited[i] = True
                result_bfs.append(i)
                queue.append(i)

result_bfs.append(v)
bfs(v)

for i in range(len(result_dfs)):
    print(result_dfs[i],end=' ') if i != len(result_dfs) - 1 else print(result_dfs[i],end='\n')

for i in result_bfs:
    print(i,end=' ')
