# 1953 (재귀함수) 삼각형 출력하기 1
# def f(n):
#     if n==1:
#         return "*"
#     else: #
#         return f(n-1)+"\n"+"*"*n # 1->2->3->4->5 순서대로 한줄씩 출력
# n=int(input())
# print(f(n))

# 3702 파스칼의 삼각형 2
# matrix = [[0]*51 for i in range(51)]
# def f(r,c):
#     if matrix[r][c]!=0: return matrix[r][c]
#
#     if r==1 or c==1: return 1 # 첫 번째 행이거나 열이면 무조건 1
#     else: matrix[r][c]=f(r,c-1)+f(r-1,c)
#
#     return matrix[r][c]%100000000
#
# r,c=map(int,input().split())
# print(f(r,c))