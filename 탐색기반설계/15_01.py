# 2641 숏다리의 계단 오르기 (Small)
# cnt=0
# N=int(input())
# def f(n, t): # 전역변수 사용 방법
#     global cnt
#     if t>0: t-=1
#     if N==n: cnt+=1
#     elif N>n:
#         if t==0: f(n+3,3)
#         f(n+2,t)
#         f(n+1,t)
#
# f(0,0)
# print(cnt)

# 2650 디지털 도어락
# def f(a,b):
#     if a<b:
#         for i in range(a,0,-1):
#             if a%i==0 and b%i==0:
#                 return i
#     else:
#         for i in range(b,0,-1):
#             if a%i==0 and b%i==0:
#                 return i
#
# a,b,c=map(int,input().split())
# temp=f(a,b)
# print("%d"%f(c,temp))

# 2651 극장 좌석 배치 1
# n,k=map(int,input().split())
# cnt,result=0,1
#
# for i in range(n,1,-1):
#     cnt+=1
#     result*=i
#     if cnt==k: break
#
# for i in range(k,0,-1):
#     result//=i
#
# print(result)