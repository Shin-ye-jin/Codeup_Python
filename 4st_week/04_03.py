# 1228 비만도 측정 1
# a,b=map(float,input().split())
# weight = (a-100)*0.9
# real = (b-weight)*100/weight
# if real>20:
#     print('비만')
# elif real>10:
#     print('과체중')
# else:
#     print('정상')

# 1229 비만도 측정 2
# a,b=map(float,input().split())
# w=0.0
# r=0.0
# if a<150:
#     w=a-100
# elif a<160:
#     w=(a-150)/2+50
# else:
#     w=(a-100)*0.9
#
# r = (b-w)*100/w
#
# if r<=10:
#     print('정상')
# elif r<=20:
#     print('과체중')
# else:
#     print('비만')

# 1230 터널 통과하기 2
# a,b,c=map(int,input().split())
# if a<=170:
#     print('CRASH',a)
# elif a>170 and b<=170:
#     print('CRASH',b)
# elif a>170 and b>170 and c<=170:
#     print('CRASH',c)
# else:
#     print('PASS')

# 1231 계산기 1
exp=input()

for i in range(0,len(exp)):
    if(exp[i]=='+'):
        n1=int(exp[:i])
        n2=int(exp[i+1:])
        result=n1+n2
        print(result)
    elif(exp[i]=='-'):
        n1 = int(exp[:i])
        n2 = int(exp[i + 1:])
        result = n1 - n2
        print(result)
    elif(exp[i]=='*'):
        n1 = int(exp[:i])
        n2 = int(exp[i + 1:])
        result = n1 * n2
        print(result)
    elif(exp[i]=='/'):
        n1 = int(exp[:i])
        n2 = int(exp[i + 1:])
        result = float(n1) / float(n2)
        print('%.2f' % result)