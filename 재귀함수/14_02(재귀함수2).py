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
# def f(n):
#     if n==1:
#         return 1
#     if n%2==1:
#         f(3 * n + 1)
#         print(3*n+1)
#     elif n%2==0:
#         f(n//2)
#         print(n//2)
# n=int(input())
# f(n)
# print(n)

# 1930 SuperSum
# dic={}
# def SuperSum(k,n):
#     if k==0:
#         return n
#     find = str(k)+'-'+str(n)
#
#     if find in dic:
#         return dic[find]
#
#     sum=0
#     for i in range(1,n+1):
#         sum+=SuperSum(k-1,i)
#         dic[find]=sum
#
#     return dic[find]

# matrix=[[0]*15 for i in range(15)]
#
# def SuperSum(k,n):
#     if k==0:
#         matrix[0][n]=n
#         return n
#
#     if matrix[k][n]==0: # 없다면 반복 실시
#         sum=0
#         for i in range(1,n+1):
#             sum+=SuperSum(k-1,i)
#         matrix[k][n]=sum
#         return sum
#     else: # 값이 있다면 해당 값을 반환
#         return matrix[k][n]
#
# while True:
#     try:
#         k, n = input().split(' ')
#         k = int(k)
#         n = int(n)
#         print(SuperSum(k,n))
#     except:
#         break