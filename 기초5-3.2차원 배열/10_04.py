# 1507 4개의 직사각형 넓이
# matrix=[[0]*100 for i in range(100)]
# count=0
#
# for i in range(4):
#     x1,y1,x2,y2=map(int,input().split()) # 4개 입력
#
#     for x in range(x1,x2):
#         for y in range(y1,y2):
#             matrix[x][y]=1 # 해당 사각형 범위를 1로 채운다
#
# for i in range(0,100):
#     for j in range(0,100):
#         if matrix[i][j]==1: # 1이라면 채워진 것이기 때문에 1씩 증가하여 범위 구하기
#             count+=1
#
# print(count)

# 1508 나도 IQ 150
# n=int(input())
# matrix=[[0]*20 for i in range(20)]
#
# for i in range(n): # 각 행의 첫 번째 값 입력 받기
#     num=int(input())
#     matrix[i][0]=num
#
# for i in range(n): # 나머지 값 계산하여 저장하기
#     for j in range(1,i+1):
#         matrix[i][j] = matrix[i][j-1]-matrix[i-1][j-1]
#
# for i in range(n): # 결과 출력하기
#     for j in range(0,i+1):
#         print(matrix[i][j],end=' ')
#     print()

# 1509 진격 후 결과
matrix=[[0]*10 for i in range(10)]
num=[0]*10
count=0

for i in range(10):
    matrix[i]=list(map(int,input().split())) # 원소 하나씩 입력 받기

num = list(map(int,input().split())) # 한줄에 여러개 입력 받을 경우

for i in range(10):
    count=0 # 처음부터 초기화 하기
    if num[i]==1: # 1일 경우만 실시
        for j in range(9,-1,-1): # 하단부터 비교
            if matrix[j][i] >0: # 장애물이 있는 경우
                count=1
                print(i+1,"crash")
                break
            elif matrix[j][i]<0: # 구덩이
                count=1
                print(i+1,"fall")
                break
        if count==0: # 안전하게 통과
            print(i+1,"safe")
