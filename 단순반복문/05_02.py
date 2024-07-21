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

# 1272 기부
a, b = map(int, input().split())
sum = 0
if a % 2 == 1:
    sum += a // 2 + 1
else:
    sum += a * 5
if b % 2 == 1:
    sum += b // 2 + 1
else:
    sum += b * 5

print(sum)

# 1273 약수 구하기
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        print(i,end=' ')

# 1274 소수 판별
a=int(input())
count=0
for i in range(2,a):
    if a%i==0:
        count += 1
if count==0:
    print("prime")
else:
    print("not prime")
