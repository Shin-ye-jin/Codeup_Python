# 1511 테두리의 합
# n = int(input())
# matrix=[[0]*n for i in range(n)]
# num=1
# result=0
#
# for i in range(n): # 배열 만들기 숫자 채우기
#     for j in range(n):
#         matrix[i][j]=num
#         num+=1
#
# for i in range(n): # 테두리 합 구하기
#     if i==0 or i==n-1: # 첫줄과 마지막 줄
#         for j in range(n):
#             result+=matrix[i][j]
#     else: # 아닐 경우 양쪽 끝만 계산
#         result=result+matrix[i][0]+matrix[i][n-1]
#
# print(result)

# 1512 숫자 등고선
n=int(input())
x,y=map(int,input().split())
matrix=[[0]*n for i in range(n)]
x=x-1 # 인덱스 맞추기
y=y-1
num=1

for i in range(n): # 기준 행 채우기
    if i<=y: # 열 기준
        matrix[x][i]=num+y-i
    else:
        matrix[x][i]=num+i-y

for i in range(n): # 기준 행을 가지고 행을 증가 감소하면서 값 채우기
    for j in range(x+1,n):
        matrix[j][i]= matrix[j-1][i]+1
    for j in range(x-1,-1,-1):
        matrix[j][i]=matrix[j+1][i]+1

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print()