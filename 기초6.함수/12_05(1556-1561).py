# 1556 [기초-함수작성] 함수로 n! 리턴하기
# def f(num):
#     result=1
#     for i in range(num,0,-1):
#         result*=i
#     return result
# n=int(input())
# print(f(n))

# 1557 [기초-함수작성] 함수로 n의 약수의 개수 리턴하기
# def f(num):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     return count
# n=int(input())
# print(f(n))

# 1558 [기초-함수작성] 함수로 정수 뒤집어 리턴하기
def f(num):
    while num!=0:
        number =num%10
        print(number,end='')
        num=num//10
n=int(input())
f(n)