from collections import deque

r, c, n = map(int,input().split())

graph = []
for i in range(r):
    graph.append(list(map(str,input())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def boom_bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = '.'
    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            # bomb
            if graph[nx][ny] == '2':
                queue.append((nx,ny))
            graph[nx][ny] = '.'

def bomb_increment():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '2':
                pass
            elif graph[i][j] == '1':
                graph[i][j] = '2'
            elif graph[i][j] == 'O':
                graph[i][j] = '1'

def bomb_install():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = 'O'

# n번 반복
for i in range(1, n+1):
    bomb_increment()
    if i == 1:
        continue
    elif i % 2 == 0:
        bomb_install()
    elif i % 2 == 1:
        for j in range(r):
            for k in range(c):
                if graph[j][k] == '2':
                    boom_bfs(j,k)

for i in range(r):
    for j in range(c):
        print('O',end='') if graph[i][j] != '.' else print('.',end='')
    print('\n',end='')