# 1901 (재귀 함수) 1부터 n까지 출력하기
# def f(n):
#     if n==0:
#         return
#     else:
#         f(n-1)
#         print(n)
#
# n=int(input())
# f(n)

# 1902 (재귀 함수) 1부터 n까지 역순으로 출력하기
# def f(n):
#     if n==0:
#         return
#     else:
#         print(n)
#         f(n-1)
# n=int(input())
# f(n)

# 1904 (재귀함수) 두 수 사이의 홀수 출력하기
# def f(a,b):
#     if a>b:
#         return
#     else:
#         if a%2==1:
#             print(a,end=' ')
#             f(a+1,b)
#         else:
#             f(a+1,b)
#
# a,b=map(int,input().split())
# f(a,b)

# 1905 (재귀함수) 1부터 n까지 합 구하기
# import sys
# sys.setrecursionlimit(100000)
#
# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n+f(n-1)
# n=int(input())
# print("%d"%f(n))

# 1912 (재귀함수) 팩토리얼 계산
# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n*f(n-1)
#
# n=int(input())
# print("%d"%f(n))

# 1916 (재귀함수) 피보나치 수열 (Large)
# a=[0]*201
# def f(n):
#     if a[n]!=0:
#         return a[n]
#     elif n<=2:
#         return 1
#     a[n] = (f(n - 1) + f(n - 2)) % 10009
#     return a[n]
#
# n=int(input())
# print("%d"%f(n))