# 1547 [기초-함수작성] 함수로 prime/composite 판별하기
# def f(num):
#     count=0
#     for i in range(2,1000001):
#         if num%i==0:
#             count+=1
#     if count==1:
#         print("prime")
#     else:
#         print("composite")
# n=int(input())
# f(n)

# 1548 [기초-함수작성] 함수로 학점 리턴하기
# def f(num):
#     if num>=90:
#         print("A")
#     elif num>=80:
#         print("B")
#     elif num>=70:
#         print("C")
#     elif num>=60:
#         print("D")
#     else:
#         print("F")
# n=int(input())
# f(n)

# 1549 [기초-함수작성] 함수로 절댓값 리턴하기
def f(num):
    if num<0:
        print(num*(-1))
    else:
        print(num)
n=int(input())
f(n)