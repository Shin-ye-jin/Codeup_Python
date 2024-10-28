# 4863 리조트



# 4866 방 배정(중등)
# n,k=map(int,input().split())
# matrix = [[0]*3 for i in range(7)]
# count=0
# for i in range(n):
#     a,b=map(int,input().split())
#     if b%2==0: b-=1
#     if b==1:
#         matrix[b][0]+=1
#     else:
#         matrix[b][a]+=1
#
# for i in range(1,7,2):
#     for j in range(2):
#         if matrix[i][j]>=1 and matrix[i][j]<=k:
#             count+=1
#         elif matrix[i][j]>k:
#             num = matrix[i][j]
#             count += num//k
#             if num%k!=0:
#                 count +=1
# print(count)

# 4876 딱지놀이

