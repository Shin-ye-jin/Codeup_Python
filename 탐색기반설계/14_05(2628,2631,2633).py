# 2628 케익 자르기
# def f(a,b,c,d):
#     count=0
#     for i in range(a+1,b+1):
#         if i==c or i==d:
#             count+=1
#     if count==1: print("cross")
#     else: print("not cross")
#
# a,b=map(int,input().split())
# c,d=map(int,input().split())
#
# if a<b: f(a,b,c,d)
# else: f(b,a,c,d)

# 2631 보물 찾기 - Hard...
# n,k=map(int, input().split())
# a=[0]
# cnt=0
# a[1:n]=[int(i) for i in input().split()]
#
# for i in range(1, n+1) :
#     a[i]+=a[i-1]
#
# t=0
# for i in range(1, n+1) :
#     while a[i]-a[t]>k :
#         t+=1
#     if a[i]-a[t]==k :
#         cnt+=1
#
# print(cnt)

# 2633 Lower Bound
n,k=map(int,input().split())
num=[int(i) for i in input().split()]
cnt=0

for i in range(0,n):
    if num[i]==k or num[i]>k:
        cnt=i+1
        break

if cnt==0: print(n+1)
else: print(cnt)