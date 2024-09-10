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

# 2652 극장 좌석 배치 2
# def f(n):
#     if n<=1: return 1
#     else: return n*f(n-1)
#
# n,k=map(int,input().split())
#
# tmp=n-k
#
# result=f(tmp+1)/(f(k)*f(tmp+1-k))
# print("%.0f"%result)

# 2653 규칙에 맞는 이진수 만들기
# n=int(input())
# tmp=2**n
# temp1=2
# cnt,result=0,0
# for i in range(tmp):
#     n2=i
#     for j in range(n):
#         temp2=n2%2
#         if temp1==0 and temp2==0: cnt+=1
#         temp1=n2%2
#         n2=n2//2
#     if cnt<1: result+=1
#     temp1=2
#     cnt=0
#
# print(result)

