# 1562 [기초-함수작성] 함수로 두 정수의 작은 값 리턴하기
# def min(n,m):
#     if n<m:
#         return n
#     else:
#         return m
# n,m=map(int,input().split())
# print(min(n,m))

# 1563 [기초-함수작성] 함수로 세 정수 중 중간 값 리턴하기
# def mid(n,m,x):
#     if n>=m:
#         if m>=x: # n>=m>=x 2
#             return m
#         elif x>=n: # x>=n>=m
#             return n
#         else: # n>=x>=m 2
#             return x
#     elif n>=x:
#         if x>=m: # n>=x>=m
#             return x
#         elif m>=n: # m>=n>=x
#             return n
#         else: # n>=m>=x
#             return m
#     elif m>=x:
#         if x>=n: # m>=x>=n
#             return x
#         elif n>=m: # n>=m>=x
#             return m
#         else: # m>=n>=x
#             return n
#     else:
#         return m # 정렬된 경우
#
# n,m,x=map(int,input().split())
# print(mid(n,m,x))

# 1564 [기초-함수작성] 함수로 최대공약수 리턴하기
# def f(n,m):
#     result=1
#     if n<m:
#         for i in range(1,n+1):
#             if n%i==0 and m%i==0:
#                 result=i
#     else:
#         for i in range(1,m+1):
#             if n%i==0 and m%i==0:
#                 result=i
#     return result
# n,m=map(int,input().split())
# print(f(n,m))