# 1550 [기초-함수작성] 함수의 양의 제곱근의 정수 부분만 리턴하기
# def f(n):
#     num=0
#     for i in range(0,n+1):
#         if i*i>n:
#             break
#         else: # i*i가 n보다 크기 직전
#             num=i
#     return num
# n=int(input())
# print(f(n))

# 1551 [기초-함수작성] 함수로 원하는 값의 위치 리턴하기 1
# def f(num,n):
#     count=0
#     for i in num:
#         count+=1
#         if i==n:
#             return count
#     return -1
# n = int(input())
# num=list(map(int,input().split()))
# k=int(input())
# print(f(num,k))

# 1552 [기초-함수작성] 함수로 소수 부분만 리턴하기
# def f(n):
#     return n-int(n)
# n=float(input())
# print("%.14f" % f(n)) # 소수점이 14자리이다.