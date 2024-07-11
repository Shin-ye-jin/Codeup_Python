# 1754 큰 수 비교
a,b,=map(int,input().split())
max=a
min=b
if max<b:
  max=b
  min=a
print(min, max)

# 1990 3의 배수 판별하기
n=int(input())
if n%3==0:
  print(1)
else:
  print(0)

# 2721 순환 문자열
a=input()
b=input()
c=input()
if a[-1]==b[0] and b[-1]==c[0] and c[-1]==a[0]:
  print("good")
else:
  print("bad")

# 6130 일차 방정식 ax+-=b=0의 해 구하기
a,b=input().split('x')

a=int(a)
b=int(b)

result = format(-b/a,".2f")
print(result)

# 6131 일차 방정식 ax+-b=c의 해 구하기
a,b=input().split('x')
b,c=b.split('=')

a=int(a)
b=int(b)
c=int(c)

num=c-b

result = format(num/a,".2f")
print(result)