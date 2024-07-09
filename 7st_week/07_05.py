# 1295 알파벳 대소문자 변환
n=input()
for i in n:
  if ord(i)>=65 and ord(i)<=90:
    print(chr(ord(i)+32),end='')
  elif ord(i)>=97 and ord(i)<=122:
    print(chr(ord(i)-32),end='')
  else:
    print(i,end='')

# 1406 love
n=input()
if n=='love':
  print('I',n,"you.")
else:
  print()

# 1407 문자열 출력하기 1
temp=list(input().split())
for i in temp:
    if i==' ':
        continue
    else:
        print(i,end='')