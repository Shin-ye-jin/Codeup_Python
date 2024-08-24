# 1571 [기초-함수작성] 함수로 Upper Bound 위치 리턴하기
# def f(n,k):
#     for i in range(n):
#         if num[i]>k:
#             return i+1
#     return n+1
#
# n=int(input())
# num=list(map(int,input().split()))
# k=int(input())
#
# print(f(n,k))

# 1576, 1577, 1578, 1579, 1580, 1581 c전용 문제

# 1602 절대값 함수
# def abs(num):
#     if num<0:
#         return (-num)
#     else:
#         return num
#
# n=float(input())
# print("%.10g"%abs(n))

# # 1610 서브 스트링
# def f(str,a,b):
#     s1=list(range(0,100))
#     j=0
#     for i in range(a,a+b):
#         s1[j]=str[i]
#         j+=1
#     return s1
#
# str=list(input()) # 띄어쓰기 없이 들어오는 경우
# str1=list(range(0,100))
# a,b=map(int,input().split())
#
# str1=f(str,a,b)
#
# for i in range(b):
#     print(str1[i],end='')

# 1615 셀프 넘버(Self-Number)
# def f(n):
#     tmp=n
#     while n!=0: # 여기 과정 다시!
#         tmp=tmp+n%10
#         n=n//10
#     num[tmp]+=1
#
# a,b=map(int,input().split())
# num=[0]*6000
# sum=0
#
# for i in range(1,b+1):
#     f(i)
# for i in range(a,b+1):
#     if num[i]==0:
#         sum+=i
# print(sum)

# 1620 자릿수의 합
def f(n):
    if n//10==0:
        return n
    else:
        return f(n//10)+f(n%10) # 몫과 나머지, 재귀함수처럼 사용

num=list(map(int,input())) # 띄어쓰기 없는 정수형
sum=0

for i in num:
    sum+=i

while sum >=10:
    sum = f(sum)

print(sum)

