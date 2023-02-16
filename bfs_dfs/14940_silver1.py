n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    data[x][y] = 0
    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if data[nx][ny] == 0 or data[nx][ny] == -2:
                continue
            elif data[nx][ny] == 1:
                if now_x == x and now_y == y:
                    data[nx][ny] = -2
                else:
                    data[nx][ny] = data[now_x][now_y] + 1 if data[now_x][now_y] != -2 else 2
                queue.append((nx,ny))

flag = False

#main
for i in range(n):
    for j in range(m):
        if flag == False:
            if data[i][j] == 2:
                bfs(i,j)
                flag = True
        else:
            break
    if flag == True:
        break
    
#print
for i in range(n):
    for j in range(m):
        if data[i][j] == -2:
            print('1',end=' ')
        elif data[i][j] == 1:
            print('-1',end=' ')
        else:
            print(data[i][j],end=' ')
    print('\n',end='')