# 1408 암호 처리
n=input()
for i in n:
  print(chr(ord(i)+2),end='')
print()
for i in n:
  print(chr(ord(i)*7%80+48),end='')

# 1414 C언어를 찾아라
n=input()
count=0
count2=0
for i in n:
  if i=='c' or i=='C':
    count+=1
for i in range(len(n)):
  if n[i:i+2]=='cc' or n[i:i+2]=='CC' or n[i:i+2]=='Cc' or n[i:i+2]=='cC':
    count2+=1
print(count)
print(count2)

# 1418 t를 찾아라
n=input()
count=0
for i in n:
  count+=1
  if i=='t':
    print(count,end=' ')

# 1419 love 2
n=input()
count=0
for i in range(len(n)):
  if n[i:i+4]=='love':
    count+=1
print(count)

# 1733 I.O.I
n=input()
if n=="IOI":
  print("IOI is the International Olympiad in Informatics.")
else:
  print("I don't care.")

# 1734 welcome!
ID=input()
print("welcome! "+ID)