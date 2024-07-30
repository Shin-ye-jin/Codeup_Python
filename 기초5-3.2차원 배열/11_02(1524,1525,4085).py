# 1524 지뢰 찾기 1
# matrix=[[0]*11 for i in range(11)]
#
# for i in range(1,10):
#     result = list(map(int,input().split()))
#     for j in range(0,9):
#         matrix[i][j+1]=result[j]
#
# r,c=map(int,input().split())
#
# num = matrix[r-1][c-1] + matrix[r][c-1]+matrix[r+1][c-1]+matrix[r-1][c]+matrix[r+1][c]+matrix[r-1][c+1]+matrix[r][c+1]+matrix[r+1][c+1]
#
# if matrix[r][c]==1:
#     print(-1)
# else:
#     print(num)

# 1525 크레이지 아케이트
matrix=[[0]*10 for i in range(10)]
for i in range(10):
    matrix[i]=list(map(int,input().split()))

n=int(input())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

