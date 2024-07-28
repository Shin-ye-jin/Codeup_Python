# 1497 [기초-배열연습] 두 개씩 묶어 큰 값 골라 배열 만들기 5-6
# n=int(input())
# num=list(map(int,input().split()))
#
# for i in range(0,len(num)-1,2):
#   if num[i]<num[i+1]:
#     print(num[i+1],end=' ')
#   else:
#     print(num[i],end=' ')

# 1498 [기초-배열연습] 여러 개씩 묶어 작은 값 골라 배열 만들기 5-7
# n,g=map(int,input().split())
# num=list(map(int,input().split()))
#
# if n%g==0:
#   for i in range(n//g):
#     result=sorted(num[i*g:(i+1)*g])
#     print(result[0],end=' ')
# else:
#   for i in range((n//g)+1):
#     if ((i+1)*g>n):
#       result=sorted(num[i*g:])
#     else:
#       result=sorted(num[i*g:(i+1)*g])
#     print(result[0],end=' ')

# 1499 [기초-배열연습] 여러 개씩 묶어 큰 값 골라 배열 만들기 5-8
n,g = map(int,input().split())
num=list(map(int,input().split()))

if n%g==0:
    for i in range(n//g):
        result=sorted(num[i*g:(i+1)*g],reverse=True) # reversed 역순 정렬
        print(result[0],end=' ')
else:
    for i in range((n//g)+1): # 홀수일 경우
        if ((i+1)*g>n):
            result=sorted(num[i*g:],reverse=True)
        else:
            result=sorted(num[i*g:(i+1)*g],reverse=True)
        print(result[0],end=' ')