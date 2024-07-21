# 1487 [기초-배열연습] 2차원 배열 달팽이 채우기 4-4
n, m = map(int, input().split())
matrix = [[0] * m for i in range(n)]
column, row, count = m - 1, -1, n * m
row_size, column_size = n, m
step = 1

while row_size and column_size:
  for _ in range(row_size):
    row += step
    matrix[row][column] = count
    count -= 1

  step = -step
  column_size -= 1

  for _ in range(column_size):
    column += step
    matrix[row][column] = count
    count -= 1

  row_size -= 1

for i in matrix:
  print(*i, ' ')

# 1488 [기초-배열연습] 2차원 배열 달팽이 채우기 4-5
n,m=map(int,input().split())
matrix = [[0]*m for i in range(n)]
column, row, count = m, n-1 , 0
row_size, column_size=n,m
step=-1

while row_size and column_size:
  for _ in range(column_size):
    count+=1
    column+=step
    matrix[row][column] = count

  row_size-=1

  for _ in range(row_size):
    count+=1
    row+=step
    matrix[row][column]=count

  step=-step
  column_size-=1

for i in matrix:
  print(*i,' ')

# 1489 [기초-배열연습] 2차원 배열 달팽이 채우기 4-6
n,m=map(int,input().split())
matrix = [[0]*m for i in range(n)]
column, row, count = m, n-1 , n*m
row_size, column_size=n,m
step=-1

while row_size and column_size:
  for _ in range(column_size):
    column+=step
    matrix[row][column] = count
    count-=1

  row_size-=1

  for _ in range(row_size):
    row+=step
    matrix[row][column]=count
    count-=1

  step=-step
  column_size-=1

for i in matrix:
  print(*i,' ')

# 1490 [기초-배열연습] 2차원 배열 달팽이 채우기 4-7
n,m=map(int,input().split())
matrix = [[0]*m for i in range(n)]
column, row, count = 0, n , 0
row_size, column_size=n,m
step=-1

while row_size and column_size:
  for _ in range(row_size):
    count+=1
    row+=step
    matrix[row][column]=count

  step=-step
  column_size-=1

  for _ in range(column_size):
    count+=1
    column+=step
    matrix[row][column] = count

  row_size-=1

for i in matrix:
  print(*i,' ')