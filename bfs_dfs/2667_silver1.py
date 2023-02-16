from collections import deque
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(graph,x,y):
    count = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if not(nx < 0 or nx >=n or ny < 0 or ny >= n):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    count += 1
                    queue.append((nx,ny))
    return count




n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))


result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph,i,j))
            

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i]) 