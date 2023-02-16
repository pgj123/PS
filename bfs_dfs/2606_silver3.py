n = int(input())
num_pair = int(input())


data = [[]]

visited = [False] * (n+1)

for i in range(n):
    data.append([])

for i in range(num_pair):
    info1, info2 = map(int,input().split())
    data[info1].append(info2)
    data[info2].append(info1)

result = 0
def dfs(node):
    global result
    visited[node] = True 
    for i in data[node]:
        if not visited[i]:
            visited[i] = True
            result += 1
            dfs(i)
    return

dfs(1)
print(result)
