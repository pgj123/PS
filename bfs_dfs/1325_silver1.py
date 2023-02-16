import sys 
from collections import deque

def bfs(node):
    queue = deque([node])
    visited = [False] * (n+1)
    visited[node] = True
    cnt = 1

    while queue:
        next = queue.popleft()
        for i in data[next]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt


input = sys.stdin.readline
n, m = map(int,input().split())
data = [[] for _ in range(n+1)]

for i in range(m):
    input1, input2 = map(int,input().split())
    data[input2].append(input1)

result = 0
ans = []

for i in range(1,n+1):
    cur = bfs(i)
    if cur > result:
        ans.clear()
        result = cur
        ans.append(i)
    elif cur == result:
        ans.append(i)

print(*ans)