# 4846 사과
# n=int(input())
# sum=0
# for i in range(n):
#     a,b=map(int,input().split())
#     sum += b%a
#
# print(sum)

# 4851 동전 게임


# 4861 방 배정
# n,k=map(int,input().split())
# matrix = [[0]*3 for i in range(7)]
# count=0
#
# for i in range(n):
#     a,b=map(int,input().split())
#     matrix[b][a]+=1
#
# for i in range(1,7):
#     for j in range(2):
#         if matrix[i][j]>=1 and matrix[i][j]<=k:
#             count+=1
#         elif matrix[i][j]>k:
#             num = matrix[i][j]
#             count += num//k
#             if num%k!=0:
#                 count+=1
#
# print(count)
