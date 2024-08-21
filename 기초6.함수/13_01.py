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
def abs(num):
    if num<0:
        return (-num)
    else:
        return num

n=float(input())
print("%.10g"%abs(n))