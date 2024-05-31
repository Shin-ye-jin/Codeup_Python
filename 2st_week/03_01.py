# 1151 10보다 작은 수
# a = int(input())
# if a<10:
#     print('small')
# else:
#     print('')

# 1152 10보다 작은 수 (else 버전)
# a=int(input())
# if a<10:
#     print('small')
# else:
#     print('big')

# 1153 두 수의 대소 비교
a,b=input().split()
a = int(a)
b = int(b)
if a>b:
    print('>')
elif b>a:
    print('<')
elif a == b:
    print('=')