import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())

title_name = []
title_power = []
characters = deque()

for i in range(n):
    name, power = map(str,input().split())
    title_name.append(name)
    title_power.append(int(power))
for i in range(m):
    characters.append(int(input()))


while characters:
    cur = characters.popleft()
    start = 0
    end = len(title_power)-1
    result_value = -1

    while start <= end:
        mid = (start + end) // 2
        if title_power[mid] < cur :
            start = mid + 1
        else:
            end = mid - 1
            result_value = mid

    
    print(title_name[result_value])