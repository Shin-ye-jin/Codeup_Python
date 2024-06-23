# 1284 암호 해독
n=int(input())
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
        print(i,end=' ')
if count==0:
    print('wrong number')