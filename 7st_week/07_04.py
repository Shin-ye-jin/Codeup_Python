# 1420 3등 찾기
# name=list(range(0,100))
# num=list(range(0,100))
# rank=list(range(0,100))
# n=int(input())
#
# for i in range(0,n):
#     name[i],num[i]=input().split()
#     rank[i]=1
#
# for i in range(0,n):
#     for j in range(0,n):
#         if int(num[i]) < int(num[j]):
#             rank[i]+=1
#
# for i in range(0,n):
#     if rank[i]==3:
#         print(name[i])

# 1425 자리 배치
# n,c=map(int,input().split())
# height=list(map(int,input().split())) # 배열 입력받기
# height.sort() # 정렬하기
#
# for i in range(0,n):
#     if (i+1)%c==0:
#         print(height[i],end=' ')
#         print()
#     else:
#         print(height[i],end=' ')

# 1440 비교
# n=int(input())
# num=list(map(int,input().split()))
#
# for i in range(0,n):
#     print("%d: "%(i+1),end='')
#     for j in range(0,n):
#         if i!=j:
#             if num[i]<num[j]:
#                 print("< ",end='')
#             if num[i]>num[j]:
#                 print("> ",end='')
#             if num[i]==num[j]:
#                 print("= ",end='')
#     print()