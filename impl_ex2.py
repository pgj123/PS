N = int(input())

full_count = 0
not_full_count = 0
if N < 3:
    full_count = 0
elif N < 13:
    full_count = 1
elif N < 23:
    full_count = 2
else:
    full_count = 3

not_full_count = N + 1 - full_count

result = full_count * 3600 + not_full_count * (60 * 15 + 45 * 15)
print(result)