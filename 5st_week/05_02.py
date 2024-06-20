# 1269 수열의 값 구하기
a,b,c,n=map(int,input().split())
for i in range(2,n+1):
    a = a*b+c
print(a)

# 1270 1의 개수는? 1
a=int(input())
count=0
for i in range(1,a+1):
    if i%10==1:
        count+=1
print(count)

# 1271 최댓값 구하기
a=int(input())
num=list(map(int,input().split()))
max=0

for i in num:
    if i>max:
        max=i
print(max)