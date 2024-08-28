# 1920 (재귀함수) 2진수 변환
# def f(n):
#     if n//2!=0:
#         f(n//2)
#     print(n%2,end='')
#
# n=int(input())
# f(n)

# 1928 (재귀함수) 우박수 (3n+1) (basic)
# def f(n):
#     if n==1:
#         return 1
#
#     if n%2==1:
#         print(3*n+1)
#         f(3*n+1)
#     elif n%2==0:
#         print(n//2)
#         f(n//2)
#
# n=int(input())
# print(n)
# f(n)

# 1929 (재귀함수) 우박수 (3n+1) (reverse)
def f(n):
    if n==1:
        return 1
    if n%2==1:
        f(3 * n + 1)
        print(3*n+1)
    elif n%2==0:
        f(n//2)
        print(n//2)
n=int(input())
f(n)
print(n)