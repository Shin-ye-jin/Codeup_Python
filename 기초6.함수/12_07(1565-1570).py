# 1565 [기초-함수작성] 함수로 최소공배수 리턴하기
# def gcd(p,q):
#     if p==0:
#         return q
#     return gcd(q%p,p)
#
# def lcm(a,b):
#     if a<b:
#         return a//gcd(b,a)*b
#     else:
#         return b//gcd(a,b)*a
#
# a,b=map(int,input().split())
# print("%d" % lcm(a,b))

# 1566 [기초-함수작성] 함수로 거듭제곱 리턴하기
# def f(a,n):
#     result=1
#     if a==1: # 1일 때 처리하기
#         return 1
#     else:
#         for i in range(1, n + 1):
#             result *= a
#         return result
#
# a,n=map(int,input().split())
# print(f(a,n))

# 1567 [기초-함수작성] 함수로 배열의 부분합 리턴하기
# def f(a,b):
#     result=0
#     for i in range(a-1,b):
#         result+=num[i]
#     return result
#
# n=int(input())
# num=list(map(int,input().split()))
# a,b=map(int,input().split())
#
# print(f(a,b))