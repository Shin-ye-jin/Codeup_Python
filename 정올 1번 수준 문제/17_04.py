# 4571 완전제곱수
# m=int(input())
# n=int(input())
# num=[0]*10000
# cnt,cnt2,sum,z=0,0,0,0
# for i in range(m,n+1):
#     for j in range(1,i+1):
#         if i%j==0: cnt+=1
#     if cnt%2==1:
#         cnt2+=1
#         num[z]=i
#         z+=1
#     cnt=0
#
# if cnt2==0:
#     print(-1)
# else:
#     for i in range(z):
#         sum+=num[i]
#     print(sum)
#     print(num[0])

# 4591 최대값 1
# num=[0]*9
#
# for i in range(9):
#     num[i]=int(input())
#
# max=num[0]
# cnt=0
#
# for i in range(1,9):
#     if max<num[i]:
#         max=num[i]
#         cnt=i
#
# print(max)
# print(cnt+1)

# 4592 색종이 1
# matrix=[[0]*100 for i in range(100)]
# n=int(input())
# cnt=0
# for i in range(n):
#     a,b,=map(int,input().split())
#     for j in range(a,a+10):
#         for k in range(b,b+10):
#             matrix[j][k]+=1
#
# for i in range(100):
#     for j in range(100):
#         if matrix[i][j]>0:
#             cnt+=1
# print(cnt)