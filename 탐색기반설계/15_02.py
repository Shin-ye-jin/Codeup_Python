# 덧셈, 뺄셈으로 n만들기
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

