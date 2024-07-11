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
