N = input()
data = [int(i) for i in input().split()]

data.sort(reverse=True)

search = 0
count = 0
while True:
    if search >= len(data) - 1:
        break
    search += data[search]
    count += 1

print(count)