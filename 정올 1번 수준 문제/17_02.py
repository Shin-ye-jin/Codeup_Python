# 4036 합과 차
# n=int(input())
# m=int(input())
#
# print((n+m)//2)
# print((n-m)//2)

# 4041 숫자 다루기
# n=int(input())
# result,cnt,re=0,0,0
# while n!=0:
#     re=re*10 + n%10
#     result+=n%10
#     n=n//10
# print(re)
# print(result)

# 4051 시간외 근무 수당
n,sum=5,0

while n!=0:
    n-=1
    s,e=map(float,input().split())
    t=e-s-1
    if t<=0.0: t=0.0
    if t>=4.0: t=4.0
    sum+= (t/0.5)*5000

if sum>=15*10000:
    sum=sum*0.95
    sum = "{:g}".format(sum)
    print(sum)
elif sum<=5*10000:
    sum = sum * 1.05
    sum = "{:g}".format(sum)
    print(sum)
else:
    sum = "{:g}".format(sum)
    print(sum)