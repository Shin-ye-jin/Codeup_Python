# 1371 마름모 출력하기
# n=int(input())
# for i in range(0,n):
#     for j in range(i,n-1):
#         print(" ",end='')
#     print("*",end='')
#
#     for j in range(0,i*2):
#         print(" ",end='')
#     print("*")
#
# for i in range(n,0,-1):
#     for j in range(0,n-i):
#         print(" ",end='')
#     print("*",end='')
#
#     for j in range(0,(i-1)*2):
#         print(" ",end='')
#     print("*")

# 1378 수열의 합
# n=int(input())
# sum=0
# s=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         s = s+j
#     sum=sum+s
#     s=0
# print(sum)

# 1380 두 주사위의 합
# k=int(input())
# for i in range(1,7):
#     for j in range(1,7):
#         if (i+j)==k:
#             print('%d %d'%(i,j))

# 1382 GuguClass
# for i in range(1,10):
#     for j in range(2,6):
#         print("%d x %d = %2d"%(j,i,i*j),end=' ')
#     print()

# 1677 종이 자르기
# m,n=map(int,input().split())
# for i in range(0,n):
#     for j in range(0,m):
#         if i==0 or i==n-1:
#             if j==0 or j==m-1:
#                 print("+",end='')
#             else:
#                 print("-",end='')
#         else:
#             if j==0 or j==m-1:
#                 print("|",end='')
#             else:
#                 print(" ",end='')
#     print()

# 3122 마름모 출력하기 2
n=int(input())
for i in range(1,n*2+1,2):
    for j in range(i,n*2-1,2):
        print(" ",end='')
    for j in range(0,i):
        print("*",end='')
    print()

for i in range(1,n):
    for j in range(0,i):
        print(" ",end='')
    for j in range(n*2-1,i*2,-1):
        print("*",end='')
    print()