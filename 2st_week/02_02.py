# 1143 비트 연산자(AND)
# a,b=input().split()
# a=int(a)
# b=int(b)
# print(a & b) # 비트연산자

# 1144 비트 연산자(OR)
# a,b=input().split()
# a=int(a)
# b=int(b)
# print(a|b)

# 1147 비트 연산자(<<)
# a,b = input().split()
# a=int(a)
# b=int(b)
# print(a << b)

# 1148 비트 연산자(>>)
# a,b=input().split()
# a=int(a)
# b=int(b)
# print(a>>b)

# 1149 두 수 중 큰 수
# a,b=input().split()
# a=int(a)
# b=int(b)
# if a>b:
#     print(a)
# else:
#     print(b)

# 1150 세 수 중 가장 작은 수
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a>b:
    if b>c :
        print(c)
    else:
        print(b)
elif a>c:
    if c>b:
        print(b)
    else:
        print(c)
else:
    if c>a:
        print(a)
    else:
        print(c)