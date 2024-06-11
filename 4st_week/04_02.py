# 1214 이 달은 며칠까지 있을까?
# year,month=map(int,input().split())
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     print('31')
# elif month==2:
#     if year%400==0 or (year%4==0 and year%100!=0):
#         print('29')
#     else:
#         print('28')
# else:
#     print('30')

# 1216 컨설팅 회사
# a,b,c=map(int,input().split())
# if a>b-c:
#     print("do not advertise")
# elif b-c>a:
#     print("advertise")
# else:
#     print("does not matter")

# 1218 삼각형 판단하기
# a,b,c=map(int,input().split())
# if a+b<=c:
#     print("삼각형아님")
# elif a==b==c:
#     print("정삼각형")
# elif a==b or b==c or a==c:
#     print("이등변삼각형")
# elif a*a+b*b==c*c:
#     print("직각삼각형")
# else:
#     print("삼각형")

# 1222 축구의 신2