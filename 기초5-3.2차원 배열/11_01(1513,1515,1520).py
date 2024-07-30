# 1513 지그재그 배열 3
# n=int(input())
# matrix=[[0]*n for i in range(n)]
# row = n-1
# column=0
# count=1
# result=n-1
#
# for i in range(n):
#     if i%2==0:
#         while column!=n:
#             matrix[row][column]=count
#             count+=1
#             row-=1
#             column+=1
#         row=row+2
#         column-=1
#     else:
#         while row!=n:
#             matrix[row][column]=count
#             count+=1
#             row+=1
#             column-=1
#         row-=1
#         column+=2
#
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j],end=' ')
#     print()

# 1515 생명 게임 1
# matrix=[[0]*27 for i in range(27)]
# r_matrix=[[0]*27 for i in range(27)]
#
# for i in range(1,26):
#     result = list(map(int,input().split()))
#     for j in range(0,25):
#         matrix[i][j+1]=result[j]
#
# for i in range(1,26):
#     for j in range(1,26):
#         life = matrix[i-1][j-1] + matrix[i][j-1]+matrix[i+1][j-1]+matrix[i-1][j]+matrix[i+1][j]+matrix[i-1][j+1]+matrix[i][j+1]+matrix[i+1][j+1]
#
#         if matrix[i][j]==0: # 생명이 없는 칸 주위 8칸에 3마리의 생명이 존재하는 경우
#             r_matrix[i][j]=1 if life==3 else 0
#         else: # 생명이 있는 칸 주위 8칸에 2마리 또는 3마리의 생명이 존재하는 경우
#             r_matrix[i][j]=1 if life==2 or life==3 else 0
#
# for i in range(1,26):
#     for j in range(1,26):
#         print(r_matrix[i][j],end=' ')
#     print()

# 1520 생명 게임 2  # 다시!! 하기!!!!!
a,b=map(int,input().split())
x,y,z=map(int,input().split())

matrix=[[0]*(b+2) for i in range(a+2)]
r_matrix=[[0]*(b+2) for i in range(a+2)]

for i in range(1,a+1):
    result = list(map(int,input().split()))
    for j in range(0,b):
        matrix[i][j+1]=result[j]

k=int(input())

for _ in range(k):
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            life = matrix[i - 1][j - 1] + matrix[i][j - 1] + matrix[i + 1][j - 1] + matrix[i - 1][j] + matrix[i + 1][j] + \
                   matrix[i - 1][j + 1] + matrix[i][j + 1] + matrix[i + 1][j + 1]

            if life == x:
                r_matrix[i][j] = 1
            elif life == z:
                r_matrix[i][j] = 0
            else:
                r_matrix[i][j] = matrix[i][j]


for i in range(1,a+1):
    for j in range(1,b+1):
        print(r_matrix[i][j],end=' ')
    print()