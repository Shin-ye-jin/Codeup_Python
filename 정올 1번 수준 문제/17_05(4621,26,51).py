# 4621 약수 구하기
# num=[0]*10000
# n,k=map(int,input().split())
# z=0
# for i in range(1,n+1):
#     if n%i==0:
#         num[z]=i
#         z+=1
#
# print(num[k-1])

# 4626 점수 계산
# n=int(input())
# num=list(map(int,input().split()))
# cnt,sum=0,0
# for i in range(0,n):
#     if num[i]==1:
#         if num[i-1]>=1 and i!=0:
#             num[i]=num[i-1]+1
#             sum+=num[i]
#         else:
#             sum+=1
# print(sum)

# 4651 윷놀이
matrix=[[0]*3 for i in range(10)]
cnt=0
for i in range(3):
    matrix[i]=list(map(int,input().split()))

for i in range(3):
    for j in range(4):
        if matrix[i][j]==1:
            cnt+=1
    if cnt==3: print("A")
    elif cnt==2: print("B")
    elif cnt==1: print("C")
    elif cnt==0: print("D")
    else: print("E")

    cnt=0