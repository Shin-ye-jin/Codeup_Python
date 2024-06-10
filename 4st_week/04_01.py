# 1207 윷놀이
# a,b,c,d=map(int,input().split())
# sum = a+b+c+d
# if sum == 0:
#     print('모')
# elif sum==1:
#     print('도')
# elif sum==2:
#     print('개')
# elif sum==3:
#     print('걸')
# else:
#     print('윷')

# 1210 칼로리 계산하기
# a,b=map(int,input().split())
# sum=0
# if a==1: sum+=400
# if a==2: sum+=340
# if a==3: sum+=170
# if a==4: sum+=100
# if a==5: sum+=70
#
# if b==1: sum+=400
# if b==2: sum+=340
# if b==3: sum+=170
# if b==4: sum+=100
# if b==5: sum+=70
#
# if sum>500:
#     print('angry')
# else:
#     print('no angry')

# 1212 삼각형의 성립 조건
a,b,c=map(int,input().split())
if c>=a and c>=b:
    if c<a+b:
        print('yes')
    else:
        print('no')
elif b>=a and b>=c:
    if b<a+c:
        print('yes')
    else:
        print('no')
elif a>=b and a>=c:
    if a<b+c:
        print('yes')
    else:
        print('no')