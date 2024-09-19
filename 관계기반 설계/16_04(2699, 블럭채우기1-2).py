# 2699 사투리
# arr = [[0]*1001 for i in range(1001)]
# s1=[0]*1001
# s2=[0]*1001
#
# s1=input()
# s2=input()
#
# len1=len(s1)
# len2=len(s2)
#
# for i in range(1,len1+1):
#     for j in range(1,len2+1):
#         if s1[i-1]==s2[j-1]:
#             arr[i][j] = arr[i-1][j-1]+1
#         else:
#             arr[i][j]=max(arr[i-1][j],arr[i][j-1])
#
# print(arr[len1][len2])

# 3709 블럭 채우기 1
# import sys
# sys.setrecursionlimit(100000)
# num = [0]*10001
#
# def f(n):
#     if n==1: return 1
#     elif n==2: return 2
#     elif num[n]==0:
#         num[n] = (f(n-2) + f(n-1)) % 100000007
#         return num[n]
#     else:
#         return num[n]
#
# n=int(input())
# print(f(n))

# 3712 블럭채우기 2
# import sys
# sys.setrecursionlimit(100000)
# num=[0]*10001
#
# def f(n):
#     if n==1 or n==2: return 0
#     elif n==3: return 2
#     elif num[n]==0:
#         num[n] = (f(n-3)*2)%100000007
#         return num[n]
#     else:
#         return num[n]
#
# n=int(input())
# print(f(n))