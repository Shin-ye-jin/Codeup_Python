#1460 [기초 배열연습] 2차원 배열 순서대로 채우기 1-1
n=int(input())
count=1
for i in range(1,n+1):
  for j in range(1,n+1):
    print(count,end=' ')
    count+=1
  print()

# 1461 [기초-배열연습] 2차원 배열 순서대로 채우기 1-2
n=int(input())
count=1*n
for i in range(1,n+1):
  for j in range(1,n+1):
    print(count,end=' ')
    count-=1
  count=n*(i+1)
  print()

# 1462 [기초-배열연습] 2차원 배열 순서대로 채우기 1-3
n = int(input())
for i in range(1, n + 1):
    count = i
    for j in range(1, n + 1):
        print(count, end=' ')
        count += n
    print()

# 1463 [기초-배열연습] 2차원 배열 순서대로 채우기 1-4
n=int(input())
for i in range(n,0,-1):
  count=i
  for j in range(1,n+1):
    print(count,end=' ')
    count+=n
  print()

# 1464 [기초-배열연습] 2차원 배열 순서대로 채우기 1-5
a,b=map(int,input().split())

for i in range(a,0,-1):
  count=b*i
  for j in range(1,b+1):
    print(count,end=' ')
    count-=1
  print()

# 1465 [기초-배열연습] 2차원 배열 순서대로 채우기 1-6
n, m = map(int, input().split())

for i in range(n-1, -1, -1):
    for j in range(1, m+1):
        print(i*m+j, end=' ')
    print()

# 1466 [기초-배열연습] 2차원 배열 순서대로 채우기 1-7
a,b=map(int,input().split())
count=a*b
for i in range(1,a+1):
  for j in range(0,b):
    print(count-(a*j),end=' ')
  count-=1
  print()