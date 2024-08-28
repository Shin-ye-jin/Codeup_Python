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