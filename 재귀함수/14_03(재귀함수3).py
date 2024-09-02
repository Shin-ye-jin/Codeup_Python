# 1953 (재귀함수) 삼각형 출력하기 1
# def f(n):
#     if n==1:
#         return "*"
#     else: #
#         return f(n-1)+"\n"+"*"*n # 1->2->3->4->5 순서대로 한줄씩 출력
# n=int(input())
# print(f(n))

# 3702 파스칼의 삼각형 2
# matrix = [[0]*51 for i in range(51)]
# def f(r,c):
#     if matrix[r][c]!=0: return matrix[r][c]
#
#     if r==1 or c==1: return 1 # 첫 번째 행이거나 열이면 무조건 1
#     else: matrix[r][c]=f(r,c-1)+f(r-1,c)
#
#     return matrix[r][c]%100000000
#
# r,c=map(int,input().split())
# print(f(r,c))

# 3704 계단 오르기 2
# import sys
# sys.setrecursionlimit(100000) # 파이썬 최대 깊이 기본 설정이 1000회이기 때문에 설정
#
# def f(n,matrix):
#     if n==1:
#         matrix[1]=1
#         return matrix[1]
#     elif n==2:
#         matrix[2]=2
#         return matrix[2]
#     elif n==3:
#         matrix[3]=4
#         return matrix[3]
#
#     if matrix[n]!=0:
#         return matrix[n]
#     else:
#         matrix[n] = (f(n - 3,matrix) + f(n - 2,matrix) + f(n - 1,matrix)) % 1000
#         return matrix[n]
#
# n=int(input())
# matrix = [0 for _ in range(n+1)]
# print(f(n,matrix))

# 3733 우박수 길이 (3n+1) (Large)
# matrix=[0]*10000001
#
# def f(n):
#     if n==1: return 1
#     if n>10000000: # 숫자가 넘으면 횟수를 추가하지 않는다.
#         if n%2==0:
#             return f(n//2)+1
#         else:
#             return f(n*3+1)+1
#
#     if matrix[n]!=0: return matrix[n]
#
#     if n%2==0:
#         matrix[n]=f(n//2)+1
#         return matrix[n]
#     else:
#         matrix[n]=f(n*3+1)+1
#         return matrix[n]
#
# count=0
# max=matrix[0]
# a,b=map(int,input().split())
#
# for i in range(a,b+1):
#     if matrix[i]==0: f(i)
#
#     if max<matrix[i]:
#         max=matrix[i]
#         count=i
#
# print(count,max)

# 4564 계단 오르기
# num=[0]*333
# s=[0]*301
#
# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
# def f(n):
#     if n<1: return 0
#     if num[n]!=0:
#         return num[n]
#     else:
#         num[n]=max(f(n-3)+s[n-1],f(n-2))+s[n]
#         return num[n]
#
#     if n==1:
#         num[1]=s[1]
#         return num[1]
#     elif n==2:
#         num[2]=s[2]+s[1]
#         return num[2]
#
# n=int(input())
# for i in range(1,n+1):
#     s[i]=int(input())
# print(f(n))