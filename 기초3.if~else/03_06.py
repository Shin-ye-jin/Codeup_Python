# 1204 영어 서수로 표현하기
# a=input()
# if int(a)==11 or int(a)==12 or int(a)==13:
#     print(a+"th")
# else:
#     if int(a)%10==1:
#         print(a+"st")
#     elif int(a)%10==2:
#         print(a+"nd")
#     elif int(a)%10==3:
#         print(a+"rd")
#     else:
#         print(a+"th")

# 1205 최댓값
# a, b = map(float, input().split())
# max = a + b;
# if a - b > max:
#     max = a - b
# if b - a > max:
#     max = b - a
# if a * b > max:
#     max = a * b
# if (a / b) > max:
#     max = a / b
# if (b / a) > max:
#     max = b / a
# if a ** b > max:
#     max = a ** b
# if b ** a > max:
#     max = b ** a
#
# print("%.6f" % max)

# 1206 배수
a,b=map(int,input().split())
if a%b==0:
    print("%d*%d=%d" % ( b,(a//b),a))
elif b%a==0:
    print("%d*%d=%d" % ( a,(b//a),b))
else:
    print('none')
