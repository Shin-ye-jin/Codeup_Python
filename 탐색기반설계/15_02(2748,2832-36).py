# 2748 덧셈, 뺄셈으로 n만들기
# num=[0]*21
# cnt=0
# m=int(input())
# n=int(input())
# if n!=0:
#     num=list(map(int,input().split()))
#
# def f(a,sum):
#     global m,cnt
#     if a<n:
#         f(a+1,sum+num[a])
#         f(a+1,sum-num[a])
#     elif sum==m: cnt+=1
#
# f(0,0)
# print(cnt)

# 2832 [상태 정의를 통한 탐색] 계잔 오르기 1-1
# def f(n,t):
#     if t<=0 and n>0:
#         return 0
#     else:
#         if n==1: return 1
#         elif n==2:
#             if t==1: return 1
#             else: return 2
#         else:
#             return f(n-2,t-1) + f(n-1,t-1)
# n,k=map(int, input().split())
# print(f(n,k-1))

# 2833 [상태 정의를 통한 탐색] 계단 오르기 2-1
# def f(n,t):
#     if t<=0 and n>0:
#         return 0
#     else:
#         if n==1: return 1
#         elif n==2:
#             if t==1: return 1
#             else: return 2
#         elif n==3:
#             if t==1: return 1
#             elif t==2: return 3
#             else: return 4
#         else:
#             return f(n-3,t-1) + f(n-2,t-1) + f(n-1,t-1)
#
# n,k=map(int, input().split())
# print(f(n,k-1))

# 2834 [상태 정의를 통하 탐색] 계단 오르기 3-1

# 2835 [상태 정의를 통한 탐색] 계단 오르기 4-1
# def f(n,k,r):
#     if n!=0 and k==0: return 0
#     elif n==0 and k!=0: return 0
#     elif n==0 and k==0: return 1
#     elif r==3:
#         return f(n-1,k-1,0)+f(n-2,k-1,1)+f(n-3,k-1,2)
#     elif r==0:
#         return f(n-2,k-1,1) + f(n-3,k-1,2)
#     elif r==1:
#         return f(n-1,k-1,0) + f(n-3,k-1,2)
#     elif r==2:
#         return f(n-1,k-1,0) + f(n-2,k-1,1)
#
# n,k=map(int,input().split())
# sum=0
# for i in range(k):
#     sum+=f(n,i,3)
# print(sum)

# 2836 [상태 정의를 통한 탐색] 계단 오르기 6-1
# def f(n,k,m):
#     if n!=0 and k==0: return 0
#     elif n==0 and k!=0: return 0
#     elif n==0 and k==0: return 1
#     elif (n-1)==m: return f(n-2,k-1,m)+f(n-3,k-1,m)
#     elif (n-2)==m: return f(n-1,k-1,m)+f(n-3,k-1,m)
#     elif (n-3)==m: return f(n-1,k-1,m)+f(n-2,k-1,m)
#     else: return f(n-1,k-1,m)+f(n-2,k-1,m)+f(n-3,k-1,m)
#
# n,m,k=map(int,input().split())
# sum=0
#
# for i in range(1,k):
#     sum+=f(n,i,m)
#
# print(sum)
