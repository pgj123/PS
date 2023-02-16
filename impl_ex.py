N = int(input())
plan = input().split()

#####서  북   동  남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

x = 1
y = 1
for i in plan:
    if i == 'U':
        y = max(1, y-1)
    if i == 'D':
        y = min(N, y+1)
    if i == 'R':
        x = min(N, x+1)
    if i == 'L':
        x = max(1, x-1)

print(f"{y} {x}")