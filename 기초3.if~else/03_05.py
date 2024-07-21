# 1172 세 수 정렬하기
# a,b,c=map(int,input().split())
# if a<=b and a<=c:
#     if b<=c:
#         print(a,b,c)
#     else:
#         print(a,c,b)
# elif b<=a and b<=c:
#     if a<=c:
#         print(b,a,c)
#     else:
#         print(b,c,a)
# else:
#     if a<=b:
#         print(c,a,b)
#     else:
#         print(c,b,a)

# 1173 30분전
# a,b=map(int,input().split())
# if b<30:
#     if a<1:
#         print(a+23,b+30)
#     else:
#         print(a-1,b+30)
# else:
#     print(a,b-30)

# 1180 만능 휴지통
# a=int(input())
# c=a//10
# d=a%10
# e=d*10+c
# f = e*2
# if f<100:
#     if f<=50:
#         print(f)
#         print("GOOD")
#     else:
#         print(f)
#         print("OH MY GOD")
# else:
#     f = f-100
#     if f<=50:
#         print(f)
#         print("GOOD")
#     else:
#         print(f)
#         print("OH MY GOD")

# 정수 판별
# a=int(input())
# if a>0:
#     print("양수")
# elif a==0:
#     print(0)
# else:
#     print("음수")

# 1202 등급 판정
# a=int(input())
# if a>=90:
#     print('A')
# elif a>=80:
#     print('B')
# elif a>=70:
#     print('C')
# elif a>=60:
#     print('D')
# else:
#     print('F')

# 1203 비만도 측정 0
# a=int(input())
# if a>20:
#     print("비만")
# elif a>10:
#     print("과체중")
# else:
#     print("정상")
