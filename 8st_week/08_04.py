# 1467 [기초-배열연습] 2차원 배열 순서대로 채우기 1-8
a,b=map(int,input().split())
count=a*(b-1)

for i in range(1,a+1):
  count+=1
  temp = count
  for j in range(0,b):
    print(temp,end=' ')
    temp-=a
  print()

# 1468 [기초-배열연습] 2차원 배열 지그재그 채우기 2-1
n=int(input())
count=0
for i in range(1,n+1):
  if i%2==1:
    count+=1
    for j in range(0,n):
      print(count,end=' ')
      count+=1
  else:
    count+=(n-1)
    temp=count
    for j in range(0,n):
      print(temp,end=' ')
      temp-=1
  print()

# 1469 [기초-배열연습] 2차원 배열 지그재그 채우기 2-2
n=int(input())
count=0
for i in range(0,n):
  if i%2==0:
    count+=n
    for j in range(0,n):
      print(count,end=' ')
      count-=1
  elif i%2==1:
    count+=(n+1)
    for j in range(0,n):
      print(count,end=' ')
      count+=1
    count-=1
  print()