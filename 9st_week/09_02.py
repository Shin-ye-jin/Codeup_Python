# 1476 [기초-배열연습] 2차원 배열 빗금 채우기 3-1
n,m=map(int,input().split())
matrix=[[0]*m for i in range(n)]
count=0

for i in range(0,n+m-1):
  for j in range(0,m):
    for k in range(0,n):
      if j+k==i:
        count+=1
        matrix[k][j]=count

for i in range(0,n):
  for j in range(0,m):
    print(matrix[i][j],end=' ')
  print()

# 1477 [기초-배열연습] 2차원 배열 빗금 채우기 3-2
n,m=map(int,input().split())
matrix = [[0]*m for i in range(n)]
count=0

for i in range(0,n+m-1):
  for j in range(0,n):  # 범위 주의
    for k in range(0,m):
      if j+k==i:
        count+=1
        matrix[j][k]=count

for i in range(0,n):
  for j in range(0,m):
    print(matrix[i][j],end=' ')
  print()

# 1478 [기초-배열연습] 2차원 배열 빗금 채우기 3-3
n,m=map(int,input().split())
matrix=[[0]*m for i in range(n)]
count=0

for i in range(0,n+m-1):
  for j in range(0,n):
    for k in range(0,m):
      if j+k==i:
        count+=1
        matrix[j][k]=count

for i in range(0,n):
  for j in range(m-1,-1,-1):
    print(matrix[i][j],end=' ')
  print()