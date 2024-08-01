# 1441 버블 정렬
# n=int(input())
# matrix=[0]*n
#
# for i in range(n):
#     num=int(input())
#     matrix[i]=num
#
# matrix.sort()
#
# # for i in range(n-1):
# #     for j in range(n-1-i):
# #         if matrix[j]>matrix[j+1]:
# #             temp=matrix[j]
# #             matrix[j]=matrix[j+1]
# #             matrix[j+1]=temp
#
# # 파이썬 정렬이 느린 관계로 sort()를 사용하여 해결
#
# for i in range(n):
#     print(matrix[i])

# 1442 선택 정렬
# 정렬되지 않은 것 중 가장 첫 번째를 기준으로 하여 최소값 찾기
# n=int(input())
# matrix=[0]*n
#
# for i in range(n):
#     num=int(input())
#     matrix[i]=num
#
# # matrix.sort - 시간 초과로 해당 코드 사용
#
# for i in range(n):
#     for j in range(i,n): # 정렬되지 않은 것중 첫 번째와 나머지 수 비교
#         if matrix[i]>matrix[j]:
#             temp=matrix[i]
#             matrix[i]=matrix[j]
#             matrix[j]=temp
#
# for i in range(n):
#     print(matrix[i])

# 1443 삽입 정렬
# 인덱스 0은 이미 정렬된 것으로 함
n=int(input())
matrix=[0]*n

for i in range(n):
    num=int(input())
    matrix[i]=num

# matirx.sort() 로 해결

for i in range(1,n):
    for j in range(i,0,-1): # 뒤에서부터 비교
        if matrix[j-1]>matrix[j]:
            temp=matrix[j-1]
            matrix[j-1]=matrix[j]
            matrix[j]=temp

for i in range(n):
    print(matrix[i])