#1460 [기초 배열연습] 2차원 배열 순서대로 채우기 1-1
n=int(input())
count=1
for i in range(1,n+1):
  for j in range(1,n+1):
    print(count,end=' ')
    count+=1
  print()
