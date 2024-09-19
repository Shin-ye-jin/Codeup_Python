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
import sys
sys.setrecursionlimit(100000)
num=[0]*10001

def f(n):
    if n==1: return 1
    elif n==2: return 2
    elif n==3: return 6
    elif num[n]==0:
        num[n]=(f(n-2)+f(n-1)+f(n-3)*3)%1000
        return num[n]
    else:
        return num[n]

n=int(input())
print(f(n))