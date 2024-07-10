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