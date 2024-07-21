# 1368 평행사변형 출력하기 2
# a,b,temp=input().split()
# a=int(a)
# b=int(b)
# if temp=="L":
#     for i in range(0,a):
#         for j in range(0,i):
#             print(" ",end='')
#         for j in range(0,b):
#             print("*",end='')
#         print()
# else:
#     for i in range(0,a):
#         for j in range(a-1,i,-1):
#             print(" ",end='')
#         for j in range(0,b):
#             print("*",end='')
#         print()

# 1369 빗금 친 사각형 출력하기
# n,k=map(int,input().split())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         for j in range(0,n):
#             print("*",end='')
#     else:
#         for j in range(0,n):
#             if j==0 or j ==n-1 or (i+j)%k==0:
#                 print("*",end='')
#             else:
#                 print(" ",end='')
#     print()

# 1370 지그재그 출력하기
h,r=map(int,input().split())
for i in range(0,r):
    for j in range(0,h):
        for k in range(0,j):
            print(" ",end='')
        print("*")
    for j in range(h-1,0,-1):
        for k in range(1,j):
            print(" ",end='')
        print("*")