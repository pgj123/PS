n = int(input())

data = [[] for _ in range(n+1)]

for i in range(n-1):
    input1, input2 = map(int,input().split())

    data[input1].append(input2)
    data[input2].append(input1)

for i in range(n+1):
    data[i].sort()

visited = [False] * (n+1)

result = [[] for _ in range(n+1)]

def dfs(node):
    visited[node] = True
    for i in data[node]:
        if visited[i]:
            result[node].append(i)
        else:
            visited[i] = True
            dfs(i)

#dfs(1)
from collections import deque
def bfs(node):
    queue = deque([node])
    visited[node] = True
    while queue:
        next = queue.popleft()
        for i in data[next]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
            else:
                result[next].append(i)

bfs(1)
for i in result[2:]:
    print(i[0])