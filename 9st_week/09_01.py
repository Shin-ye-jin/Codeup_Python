# 1470 [기초-배열연습] 2차원 배열 지그재그 채우기 2-3
n = int(input())
matrix = [[0] * n for i in range(n)]
count = 0

for i in range(0, n):
  if i % 2 == 1:
    for j in range(n - 1, -1, -1):
      count += 1
      matrix[i][j] = count
  else:
    for j in range(0, n):
      count += 1
      matrix[i][j] = count

for i in range(0, n):
  for j in range(0, n):
    print(matrix[j][i], end=' ')
  print()

# 1471 [기초-배열연습] 2차원 배열 지그재그 채우기 2-4
n=int(input())
matrix=[[0]*n for i in range(n)]
count=0

for i in range(0,n):
  if i%2==1:
    for j in range(0,n):
      count+=1
      matrix[i][j]=count
  else:
    for j in range(n-1,-1,-1):
      count+=1
      matrix[i][j]=count

for i in range(0,n):
  for j in range(0,n):
    print(matrix[j][i],end=' ')
  print()

 # 1472 [기초-배열연습] 2차원 배열 지그재그 채우기 2-5
n, m = map(int, input().split())
matrix = [[0] * m for i in range(n)]
count = 0

for i in range(0, n):
    if i % 2 == 1:
        for j in range(0, m):
            count += 1
            matrix[i][j] = count
    else:
        for j in range(m - 1, -1, -1):
            count += 1
            matrix[i][j] = count

for i in range(n - 1, -1, -1):
    for j in range(0, m):
        print(matrix[i][j], end=' ')
    print()