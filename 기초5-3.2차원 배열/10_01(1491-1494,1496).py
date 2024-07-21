# 1491 [기초-배열연습] 2차원 배열 달팽이 채우기 4-8
# n,m=map(int,input().split())
# matrix = [[0]*m for i in range(n)]
# column, row, count = 0, n , n*m
# row_size, column_size=n,m
# step=-1
#
# while row_size and column_size:
#   for _ in range(row_size):
#     row+=step
#     matrix[row][column]=count
#     count-=1
#
#   step=-step
#   column_size-=1
#
#   for _ in range(column_size):
#     column+=step
#     matrix[row][column] = count
#     count-=1
#
#   row_size-=1
#
# for i in matrix:
#   print(*i,' ')

# 1492 [기초-배열연습] 1차원 누적 합배열 만들기 5-1
# n=int(input())
# num=list(map(int,input().split()))
# sum=0
# for i in num:
#   sum+=i
#   print(sum,end=' ')

# 1493 [기초-배열연습] 2차원 누적 합배열 만들기 5-2
n,m=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)] # 2차원 배열 입력받기
arr2 = [[0]*m for _ in range(n)]
sum=0
nsum=0

for i in range(n):
  for j in range(m):
      sum+=arr[i][j]
      arr2[i][j]=sum
  sum=0

for i in range(n):
  for j in range(m):
    if i==0:
      print(arr2[i][j],end=' ')
    else:
      sum= arr2[i][j]+arr2[i-1][j]
      arr2[i][j]=sum
      print(sum,end=' ')
  print()

# 1494 [기초-배열연습] 1차원 차이 배열 만들기 5-3
n,k=map(int,input().split())
d=[0]*(n+1)
num=[0]*(n+1)

for i in range(k):
  s,e,u=map(int,input().split())
  d[s-1]=d[s-1]+u
  d[e]=d[e]-u

for i in range(0,n):
  print(d[i],end=' ')

print()

for i in range(0,n):
  if i==0:
    num[i]=d[i]
    print(num[i],end=' ')
  else:
    num[i]=num[i-1]+d[i]
    print(num[i],end=' ')

# 1496 [기초-배열연습] 두 개씩 묶어 작은 값 골라 배열 만들기 5-5
n=int(input())
num=list(map(int,input().split()))

for i in range(0,len(num)-1,2):
  if num[i]>num[i+1]:
    print(num[i+1],end=' ')
  else:
    print(num[i],end=' ')
