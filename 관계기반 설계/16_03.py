# 1925 ( 재귀함수 ) nCr (Small)
# def f(n,r):
#     if n==r or r==0: return 1
#     else:
#         return f(n-1,r-1) + f(n-1,r)
#
# n,r=map(int,input().split())
# result=f(n,r)
# print(result)

# 1936 ( 재귀함수 ) 두 노드간의 거리
# sum=0
# def f(a,b):
#     global sum
#     if a==b: return
#     else:
#         if a>b:
#             sum+=1
#             f(a//2,b)
#         else:
#             sum+=1
#             f(a,b//2)
#
# a,b=map(int,input().split())
# f(a,b)
# print(sum)

# 2632 계단 오르기 1
# def f(n):
#     if n==1 : return 1
#     elif n==2: return 2
#     else: return f(n-2)+f(n-1)
#
# n=int(input())
# res=f(n)
# print(res)
