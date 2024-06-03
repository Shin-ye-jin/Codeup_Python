# # 1160 아르바이트 가는 날
# a=int(input())
# if (a == 1) or (a== 3) or (a==5) or (a==7):
#     print('oh my god')
# else:
#     print('enjoy')

# 1161 홀수와 짝수 그리고 더하기
# a,b=map(int,input().split())
# if a%2==0:
#     if b%2==0:
#         print("짝수+짝수=짝수")
#     else:
#         print("짝수+홀수=홀수")
# else:
#     if b%2==0:
#         print("홀수+짝수=홀수")
#     else:
#         print("홀수+홀수=짝수")

# 1162 당신의 사주를 봐 드립니다 1
y,m,d=map(int,input().split())
if((y-m+d)%10==0):
    print('대박')
else:
    print('그럭저럭')
