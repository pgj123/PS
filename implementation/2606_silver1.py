n = int(input())
num_pair = int(input())

graph = []

visited = [False] * (num_pair + 1)
for i in range(num_pair):
    graph.append(list(map(int,input().split())))


result = 0

def bfs(i, start):
    global result
    if graph[i][0] == start or graph[i][1] == start:
        next = graph[i][0] if graph[i][1] == start else graph[i][1]
        if visited[next] == False:
            result += 1
        bfs(start, next)

for i in range(num_pair):
    bfs(i, 1)

print(result)