# 3002 기억력 테스트 3
# a=[0]*1000000
# n=int(input())
# a=list(map(int,input().split()))
# m=int(input())
# tmp=list(map(int,input().split()))
#
#
# def f(start,end,res):
#     m=(start+end)//2
#     if start>end: return -1
#     elif a[m]==res:
#         return m+1
#     elif a[m]<res:
#         return f(m+1,end,res)
#     else:
#         return f(start,m-1,res)
#
# for i in range(m):
#     res=f(0,n-1,tmp[i])
#     print(res,end=' ')

# 3009 부분수열의 합
# cnt=0
# num=[0]*21
# n,s=map(int,input().split())
# num=list(map(int,input().split()))
#
# def f(a,b,sum):
#     global cnt
#     sum+=num[a]*b
#
#     if a==(n-1):
#         if sum==s: cnt+=1
#         return
#     else:
#         f(a+1,0,sum)
#         f(a+1,1,sum)
#
# f(0,1,0)
# f(0,0,0)
#
# print(cnt-(not s)*1)

