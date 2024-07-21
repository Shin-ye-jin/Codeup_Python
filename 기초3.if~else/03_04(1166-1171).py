# # 1166 윤년 판별
# a=int(input())
# if a%400==0:
#     print("Leap")
# elif a%4==0 and a%100 !=0:
#     print("Leap")
# else:
#     print("Normal")

# 1167 두 번째 수
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

# 1169 나이 계산2
# a=int(input())
# num=a-13
# if num>0:
#     print(100-num,1)
# else:
#     print(0-num,3)

# 1170 당신의 학번은? 1
# a,b,c=input().split()
# if int(c)<10:
#     print(a+b+"0"+c)
# else:
#     print(a+b+c)

# 1171 당신의 학번은? 2
# a,b,c=input().split()
# if int(b)<10:
#     if int(c)<10:
#         print(a+"0"+b+"00"+c)
#     elif int(c)<100:
#         print(a+"0"+b+"0"+c)
#     else:
#         print(a+"0"+b+c)
# else:
#     if int(c)<10:
#         print(a+b+"00"+c)
#     elif int(c)<100:
#         print(a+b+"0"+c)
#     else:
#         print(a+b+c)
