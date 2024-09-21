# 4531 대표 값
# num=[0]*5
# re=0
# for i in range(5):
#     num[i] = int(input())
#     re+=num[i]
#
# print(re//5)
#
# num=sorted(num)
# print(num[2])

# 4536 대표값 - 스페셜 저지

# 4561 홀수
# num=[0]*7
# z,ret,cnt=0,0,0
# for i in range(7):
#     n=int(input())
#     if n%2==1:
#         cnt+=1
#         num[z]=n
#         ret+=num[z]
#         z+=1
#
# if cnt==0:
#     print("-1")
# else:
#     print(ret)
#     min=num[0]
#
#     for i in range(1,z):
#         if min>num[i]:
#             min=num[i]
#     print(min)

# 4566 소수
# m=int(input())
# n=int(input())
# num=[0]*10000
# cnt,z,sum=0,0,0
#
# for i in range(m,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             cnt+=1
#             continue
#     if cnt==0 and i!=1:
#         num[z]=i
#         z+=1
#     cnt=0
#
# for i in range(z):
#     sum+=num[i]
#
# print(sum)
# print(num[0])