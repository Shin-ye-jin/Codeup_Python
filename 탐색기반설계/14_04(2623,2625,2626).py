# 2623 최대공약수 구하기
# a,b=map(int,input().split())
# count=0
#
# if a<b:
#     for i in range(a,0,-1):
#         if a%i==0 and b%i==0:
#             count+=1
#             print(i)
#             break
#
#
# else:
#     for i in range(b,0,-1):
#         if a%i==0 and b%i==0:
#             count+=1
#             print(i)
#             break
#
# if count==0: print("1")

# 2625 삼각화단 만들기 (Small)
# n=int(input())
# count=0
#
# for i in range(1,n):
#     for j in range(0,n):
#         for k in range(j,n):
#             if i<=j and i+j>k and i+j+k==n:
#                 count+=1
#
# print(count)

# 2626 (python) 삼각화단 만들기 (Large)
n=int(input())
count=0

for i in range(n//3,n//2+1):
    for j in range(1,n//3+1):
        k=n-i-j
        if j<=k and k<=i and j+k>i:
            count+=1

print(count)