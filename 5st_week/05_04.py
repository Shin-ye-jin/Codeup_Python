# 1281 홀수는 더하고 짝수는 빼고 3
# a,b=map(int,input().split())
# sum=0
# if a%2==1:
#     sum+=a
#     print(a,end='')
# else:
#     sum-=a
#     print('-%d'%a,end='')
#
# for i in range(a+1,b+1):
#     if i%2==1:
#         sum+=i
#         print('+%d'%i,end='')
#     else:
#         sum-=i
#         print('-%d'%i,end='')
# print('=%d'%sum,end='')

# 1282 제곱수 만들기
# n=int(input())
# i=0
# while True:
#     i+=1
#     if n>=i*i and n<(i+1)*(i+1):
#         print('%d'%(n-i*i),'%d'%i) # 출력 확인
#         break

# 1283 주식 투자
n=int(input())
num=int(input())
number=list(map(int,input().split()))
result = n

for i in number:
    if i>0:
        n=n+n*i*0.01
    else:
        n=n+n*i*0.01
result = result - n

if result>0:
    print("-%.0f"%result)
    print('bad')
elif result<0:
    result=result*(-1)
    print('%.0f'%result)
    print('good')
else:
    print('%.0f'%result)
    print('same')