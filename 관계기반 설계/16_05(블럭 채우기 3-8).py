# 3713 블럭 채우기 3
# import sys
# sys.setrecursionlimit(100000)
#
# num=[0]*10001
#
# def f(n):
#     if n==0 or n==1: return 1
#     elif num[n]==0:
#         num[n] = (f(n-2)*2 + f(n-1))%100007
#         return num[n]
#     else:
#         return num[n]
#
# n=int(input())
# print(f(n))

# 3714 블럭 채우기 4
# import sys
# sys.setrecursionlimit(100000)
# num=[0]*10001
#
# def f(n):
#     if n==1: return 1
#     elif n==2: return 5
#     elif n==3: return 11
#     elif num[n]==0:
#         num[n]=(f(n-3)*2 + f(n-2)*4 + f(n-1)) % 100007
#         return num[n]
#     else:
#         return num[n]
#
# n=int(input())
# print(f(n))

# 3716 블럭 채우기 5
# import sys
# sys.setrecursionlimit(100000)
# num=[0]*10001
#
# def f(n):
#     if n==1: return 1
#     elif n==2: return 2
#     elif n==3: return 6
#     elif num[n]==0:
#         num[n]=(f(n-2)+f(n-1)+f(n-3)*3)%1000
#         return num[n]
#     else:
#         return num[n]
#
# n=int(input())
# print(f(n))

# 3719 블럭 채우기 6
# import sys
# sys.setrecursionlimit(100000)
# num = [0]*10001
#
# def f(n):
#     if n==1: return 2
#     elif n==2: return 7
#     elif n==3: return 22
#     elif num[n]==0:
#         num[n] = (f(n-1)*3 + f(n-2)-f(n-3))%100007
#         return num[n]
#     else:
#         return num[n]
#
# n=int(input())
# print(f(n))

# 3721 블럭 채우기 7
# import sys
# sys.setrecursionlimit(100000)
# num=[0]*10001
# num[2] = 3
# def f(n):
#     if num[n] !=0: return num[n]
#
#     if n%2==1:
#         num[n]=0
#         return num[n]
#
#     sum=0
#
#     for i in range(2,n-1,2):
#         if i==2: sum+=f(n-i)*3
#         else: sum+=f(n-i)*2
#
#     num[n]=(sum+2)%100007
#     return num[n]
#
# n=int(input())
# print(f(n))

# 3728 블럭 채우기 8 - 시간초과
# import sys
# sys.setrecursionlimit(100000)
# num=[0]*10001
# num[1]=1
# num[2]=5
# def f(n):
#     if num[n]!=0: return num[n]
#
#     sum=0
#
#     for i in range(1,n):
#         if i==1: sum+=f(n-i)
#         elif i==2: sum+=f(n-i)*4
#         else:
#             if i%2==0: sum+=f(n-i)*3
#             else: sum+=f(n-i)*2
#
#     num[n]= (sum+3) % 100007 if n%2==0 else (sum+2)%100007
#     return num[n]
#
# n=int(input())
# print(f(n))