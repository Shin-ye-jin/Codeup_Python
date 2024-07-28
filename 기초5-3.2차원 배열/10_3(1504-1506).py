# 1504 지그재그 배열2
# n = int(input())
# num=[[0]*n for _ in range(n)]
# count=1
#
# for i in range(n):
#     if i%2==0:
#         for j in range(n):
#             num[i][j]=count
#             count+=1
#     else:
#         for j in range(n-1,-1,-1):
#             num[i][j]=count
#             count+=1
#
# for i in range(n):
#     for j in range(n):
#         print(num[j][i],end=' ')
#     print()

# 1505 2차원 배열 채우기 3(달팽이 배열)
# n=int(input())
# matrix = [[0]*n for i in range(n)]
# row, column, count = 0, -1 , 0
# row_size, column_size=n,n
# step=1
#
# while row_size and column_size:
#   for _ in range(column_size):
#     count+=1
#     column+=step
#     matrix[row][column]=count
#
#   row_size-=1
#
#   for _ in range(row_size):
#     count+=1
#     row+=step
#     matrix[row][column] = count
#
#   column_size-=1
#   step=-step
#
# for i in matrix:
#   print(*i,' ')

# 1506 2차원 배열 채우기 4(역달팽이 배열)
n=int(input())
matrix = [[0]*n for i in range(n)]
row, column, count = 0, -1 , 0
row_size, column_size=n,n
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

for i in range(n):
    for j in range(n):
        print(matrix[j][i],end=' ')
    print()