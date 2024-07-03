# 1402 거꾸로 출력하기 3
# n=int(input())
# num=list(map(int,input().split()))
# for i in range(n-1,-1,-1):
#     print(num[i],end=' ')

# 1403 배열 두번 출력하기
# n=int(input())
# num=list(map(int,input().split()))
# for i in range(0,n):
#     print(num[i])
# for i in range(0,n):
#     print(num[i])

# 1405 숫자 로테이션
# n=int(input())
# num=list(map(int,input().split()))
# index=0
# for z in range(0,n):
#     index=z
#     for j in range(0,n):
#         print(num[index],end=' ')
#         index+=1
#         if index==n:
#             index=0
#     print()