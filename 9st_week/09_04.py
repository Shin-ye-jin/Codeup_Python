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