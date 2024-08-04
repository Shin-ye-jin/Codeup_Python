# 1529 [기초-함수작성] 함수로 ** 문자 출력하기
# def f():
#     print("**")
# f()

# 1530 [기초-함수작성] 함수로 문자 A 리턴하기
# def f():
#     return 'A'
# print(f())

# 1531 [기초-함수작성] 함수로 정수(int) 1 리턴하기
# def f():
#     return 1
# print(f())

# 1532 [기초-함수작성] 함수로 정수(long long int) -2147483649 리턴하기
# def f():
#     return -2147483649
# print(f())

# 1533 [기초-함수작성] 함수로 실수(float) 3.14 리턴하기
# def f():
#     return 3.14
# print(format(f(),".6f")) # 뒤를 0으로 채우기

# 1534 [기초-함수작성] 함수로 실수(double) 3.1415926535897 리턴하기
# def f():
#     return 3.1415926535897
# print(f())

# 1535 [기초-함수작성] 함수로 가장 큰 값 위치 리턴하기
# n = int(input())
# num=list(map(int,input().split()))
# def f():
#     count = 0
#     number = 0
#     max = num[0]
#     for i in range(n):
#         if max<num[i]:
#             max = num[i]
#             count=count+1
#             number = i
#     if count==0:
#         return 1
#     else:
#         return number+1
# print(f())

# 1536 [기초-함수작성] 함수로 가장 작은 값 리턴하기
# n = int(input())
# num=list(map(int,input().split()))
#
# def f():
#     count=0
#     min = num[0]
#     for i in range(n):
#         if min>num[i]:
#             min = num[i]
#             count = count+1
#     return min
# print(f())

# 1537 [기초-함수작성] 함수로 hello 또는 world 출력하기
# n = int(input())
#
# def f(num):
#     if num==1:
#         print("hello")
#     elif num==2:
#         print("world")
# f(n)