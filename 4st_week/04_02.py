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
# a,b,c=map(int,input().split())
# count=(89-a)//5+1
# if count+b>c:
#     print("win")
# elif count+b==c:
#     print("same")
# else:
#     print("lose")

# 1224 분수 크기 비교
# a,b,c,d=map(float,input().split())
# if a/b > c/d:
#     print('>')
# elif a/b == c/d:
#     print('=')
# else:
#     print('<')

# 1226 이번 주 로또
a,b,c,d,e,f,g = map(int,input().split())
num1,num2,num3,num4,num5,num6 = map(int,input().split())
count=0
bonus=0
if num1==a or num1==b or num1==c or num1==d or num1==e or num1==f:
    count+=1
if num2==a or num2==b or num2==c or num2==d or num2==e or num2==f:
    count+=1
if num3==a or num3==b or num3==c or num3==d or num3==e or num3==f:
    count+=1
if num4==a or num4==b or num4==c or num4==d or num4==e or num4==f:
    count+=1
if num5==a or num5==b or num5==c or num5==d or num5==e or num5==f:
    count+=1
if num6==a or num6==b or num6==c or num6==d or num6==e or num6==f:
    count+=1
if num1 == g or num2 == g or num3 == g or num4 == g or num5 == g or num6 == g:
    bonus=1

if count==6:
    print('1')
elif count==5 and bonus==1:
    print('2')
elif count==5:
    print('3')
elif count==4:
    print('4')
elif count==3:
    print('5')
else:
    print('0')
