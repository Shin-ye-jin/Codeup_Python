# # 1166 윤년 판별
# a=int(input())
# if a%400==0:
#     print("Leap")
# elif a%4==0 and a%100 !=0:
#     print("Leap")
# else:
#     print("Normal")

# 두 번째 수
# a,b,c=map(int,input().split())
# if a<=b and a<=c:
#     if b<=c:
#         print(b)
#     else:
#         print(c)
# elif b<=a and b<=c:
#     if a<=c:
#         print(a)
#     else:
#         print(c)
# else:
#     if a<=b:
#         print(a)
#     else:
#         print(b)

# 1168 나이 계산1
# a,b=map(int,input().split())
# if b==1 or b==2:
#     print(100-a//10000+13)
# else:
#     print(12-a//10000+1)
