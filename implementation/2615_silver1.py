data = []
for i in range(19):
    data.append([int(i) for i in input().split()])

data2 = []
for i in range(19):
  temp = []
  for j in range(19):
    temp.append(data[j][i])
  data2.append(temp)


found = 0
found_i = 0
found_j = 0

for i in range(19):
  for j in range(19):
    if data2[i][j] > 0 :
      key = data2[i][j]

      #왼쪽 아래로 탐색
      point_i = i
      point_j = j
      vic_count = 1
      while True:
        point_j -= 1
        point_i += 1
        if point_j > -1 and point_i < 19:
          if data2[point_i][point_j] == key:
            vic_count += 1
          else:
            if vic_count > 5:
              break
        else:
          if vic_count == 5:
            found = key
            found_i = j + 1
            found_j = i + 1
          break

      if found > 0:
        break
      #직선 아래로 탐색
      point_i = i
      point_j = j
      vic_count = 1
      while True:
        point_i += 1
        if point_i < 19:
          if data2[point_i][point_j] ==key:
            vic_count += 1
          else:
            if vic_count > 5:
              break
        else:
          if vic_count == 5:
            found = key
            found_i = j + 1
            found_j = i + 1
          break

      if found > 0:
        break
      #오른쪽 아래로 탐색
      point_i = i
      point_j = j
      vic_count = 1
      while True:
        point_i += 1
        point_j += 1
        if point_i < 19 and point_j < 19:
          if data2[point_i][point_j] ==key:
            vic_count += 1
          else:
            if vic_count > 5:
              break
        else:
          if vic_count == 5:
            found = key
            found_i = j + 1
            found_j = i + 1
          break
if found > 0:
  print(f"{found}\n{found_i} {found_j}")
else:
  print(found)