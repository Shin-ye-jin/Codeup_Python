# 1482 [기초-배열연습] 2차원 배열 빗금 채우기 3-7
n,m=map(int,input().split())
matrix=[[0]*m for i in range(n)]
count=0

for i in range(0,n+m-1):
  for j in range(0,n):
    for k in range(0,m):
      if j+k==i:
        count+=1
        matrix[j][k]=count

for i in range(n-1,-1,-1):
  for j in range(0,m):
    print(matrix[i][j],end=' ')
  print()

# 1483 [기초-배열연습] 2차원 배열 빗금 채우기 3-8
n,m=map(int,input().split())
matrix=[[0]*m for i in range(n)]
count=0

for i in range(0,n+m-1):
  for j in range(0,m):
    for k in range(0,n):
      if j+k==i:
        count+=1
        matrix[k][j]=count

for i in range(n-1,-1,-1):
  for j in range(0,m):
    print(matrix[i][j],end=' ')
  print()

# 1484 [기초-배열연습] 2차원 배열 달팽이 채우기 4-1
n,m=map(int,input().split())
matrix = [[0]*m for i in range(n)]
row, column, count = 0, -1 , 0
row_size, column_size=n,m
step=1

while row_size and column_size:
  for _ in range(column_size):
    count+=1
    column+=step
    matrix[row][column]=count

  row_size-=1

  for _ in range(row_size):
    count+=1
    row+=step
    matrix[row][column] = count

  column_size-=1
  step=-step

for i in matrix:
  print(*i,' ')
