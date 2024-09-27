# 4741 오븐 시계
# a,b=map(int,input().split())
# c=int(input())
#
# b+=c
#
# if b>=60:
#     n=b//60
#     b=b%60
#     a+=n
#     if a>=24:
#         a-=24
#         print(a,b)
#     else:
#         print(a,b)
# else:
#     print(a,b)

# 4746 인공지능 시계
# a,b,c=map(int,input().split())
# d=int(input())
#
# n1=d//60
# n2=d%60
#
# b+=n1
# c+=n2
#
# if c>=60:
#     n4=c//60
#     c%=60
#     b+=n4
#     if b>=60:
#         n3=b//60
#         b%=60
#         a+=n3
#         if a>=24:
#             a%=24
#             print(a,b,c)
#         else:
#             print(a,b,c)
#     else:
#         print(a,b,c)
# else:
#     if b>=60:
#         n3=b//60
#         b%=60
#         a+=n3
#         if a>=24:
#             a%=24
#             print(a,b,c)
#         else:
#             print(a,b,c)
#     else:
#         print(a,b,c)

# 4751 아시아 정보올림피아드

# 4771 그릇
# matrix=list(input())
# res=10
# for i in range(1,len(matrix)):
#     if matrix[i]==matrix[i-1]:
#         res+=5
#     else: res+=10
#
# print(res)

# 4776 간지
# n=int(input())
# n1 = chr(ord("A")+(n+8)%12)
# n2 = 0+(n+6)%10
# print(n1,end='')
# print(n2)

# 4891 행복
# n=int(input())
# matrix = list(map(int,input().split()))
# matrix = sorted(matrix)
# m = len(matrix)
# print(matrix[m-1] - matrix[0])
