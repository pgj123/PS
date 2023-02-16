n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y,count):
    if x>=n or y>=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1,y,count+1)
        dfs(x,y+1,count+1)
        if x == n-1 and y == m-1:
            return count
    return False

result = dfs(0,0,1)
print(result)