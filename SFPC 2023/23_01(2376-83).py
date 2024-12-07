# 2376 군산스탬프투어 2
# from itertools import permutations
#
# n,m,t = map(int,input().split())
# matrix = list(map(int,input().split()))
# list_matrix = list(permutations(matrix,m))
# sum,result=5,0
# for i in range(len(list_matrix)):
#     for j in range(m):
#         sum+=list_matrix[i][j]
#     sum=sum+5*m
#     if sum<=t:
#         result+=1
#     sum=5
#
# print(result)
# 2377 임실 치즈 0 (스페셜 저지)



# 2378 임실 치즈 1
# n=int(input())
# ml = [25,15,10]
# kg = 10*n
# result = 0
# for i in range(3):
#     result = result + kg//ml[i]
#     kg = kg%ml[i]
# if kg == 0 : print(result)
# else: print(result+1)


# 2379 임실 치즈 2
# n=int(input())
# ml = [25,15,10]
# kg = 10*n
# result = 0
# for i in range(3):
#     result = result + kg//ml[i]
#     kg = kg%ml[i]
# if kg == 0 : print(result)
# else: print(result+1)


# 2380 롱케이크 0 (스페셜 저지)



# 2381 롱케이크 1
# n=int(input())
# matrix = list(map(int,input().split()))
# count=[[0]*3 for i in range(n+2)]
# c1, c2 = 0,0
# for i in matrix:
#     if count[i-1][2] == 0 and count[i+1][1] == 0:
#         count[i][1]=1
#         count[i][2]=1
#     elif count[i-1][2] == 1 and count[i+1][1] == 0:
#         count[i][2]=1
#     elif count[i-1][2] == 0 and count[i+1][1] == 1:
#         count[i][1]=1
# count[1][1], count[n][2] = 0,0
#
# for i in range(1,n+1):
#     if count[i][1]+count[i][2] == 2:
#         c2 += 1
#     elif count[i][1]+count[i][2]==1:
#         c1 += 1
# print(c1,c2)


# 2382 흑백 이미지 생성 0 (스페셜 저지)



# 2383 흑백 이미지 생성 1
# h,w = map(int,input().split())
# res = [[0]*(w+1) for i in range(h+1)]
# n = int(input())
# for i in range(n):
#     matrix = list(map(int,input().split()))
#     for j in range(matrix[0],matrix[2]+1):
#         for z in range(matrix[1],matrix[3]+1):
#             if res[j][z] == 0:
#                 res[j][z]=1
#             else:
#                 res[j][z]=0
#
# for i in range(1,h+1):
#     for j in range(1,w+1):
#         print(res[i][j],end=' ')
#     print()
h,w = map(int,input().split())
res = [[0]*(w+1) for i in range(h+1)]
n = int(input())
matrix=[0]
for i in range(n):
   x1,y1,x2,y2 = map(int,input().split())
   for j in range(x1,x2+1):
       for z in range(y1,y2+1):
           if res[j][z] == 0:
               res[j][z] = 1
           else:
               res[j][z] = 0

for i in range(1,h+1):
    for j in range(1,w+1):
        print(res[i][j],end=' ')
    print()

