# 1351 구구단 출력하기 2
# a,b=map(int,input().split())
# for i in range(a,b+1):
#     for j in range(1,10):
#         print("%d*%d=%d" % (i,j,i*j))

# 1352 사각형 출력하기 1
# a=int(input())
# for i in range(0,a):
#     for j in range(0,a):
#         print('*',end='')
#     print()

# 1353 삼각형 출력하기 1
# a=int(input())
# for i in range(1,a+1):
#     for j in range(0,i):
#         print('*',end='')
#     print()

# 1354 삼각형 출력하기 2
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print('*',end='')
#     print()

# 1355 삼각형 출력하기 3
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(0,n-i):
#         print(' ',end='')
#     for j in range(0,i):
#         print("*",end='')
#     print()

# 1356 사각형 출력하기 2
# n=int(input())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         for j in range(0,n):
#             print('*',end='')
#     else:
#         for j in range(1,n+1):
#             if j==1 or j==n:
#                 print("*",end='')
#             else:
#                 print(" ",end='')
#     print()