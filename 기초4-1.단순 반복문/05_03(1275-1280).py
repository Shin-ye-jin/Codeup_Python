# 1275 K 제곱 구하기
# n,k=map(int,input().split())
# result=1
# for i in range(0,k):
#     result=result*n
# print(result)

# 1276 팩토리얼 계산
# n=int(input())
# result=1
# for i in range(n,0,-1): # 감소
#     result=result*i
# print(result)

# 1277 몇 번째 데이터 출력하기
# n=int(input())
# number=list(map(int,input().split()))
# print(number[0],number[n//2],number[len(number)-1])

# 1278 자릿수 계산
# n=int(input())
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)

# 1279 홀수는 더하고 짝수는 빼고 1
# a,b=map(int,input().split())
# sum=0
# for i in range(a,b+1):
#     if i%2==1:
#         sum+=i
#     else:
#         sum-=i
# print(sum)

# 1280 홀수는 더하고 짝수는 빼고 2
# a,b=map(int,input().split())
# sum=0
# for i in range(a,b+1):
#     if i%2==1:
#         sum+=i
#         print('+%d' % i,end='')
#     else:
#         sum-=i
#         print('-%d' %i, end='')
# print('=%d' % sum)