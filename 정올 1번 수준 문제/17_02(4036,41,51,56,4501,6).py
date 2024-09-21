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
# n,sum=5,0
#
# while n!=0:
#     n-=1
#     s,e=map(float,input().split())
#     t=e-s-1
#     if t<=0.0: t=0.0
#     if t>=4.0: t=4.0
#     sum+= (t/0.5)*5000
#
# if sum>=15*10000:
#     sum=sum*0.95
#     sum = "{:g}".format(sum)
#     print(sum)
# elif sum<=5*10000:
#     sum = sum * 1.05
#     sum = "{:g}".format(sum)
#     print(sum)
# else:
#     sum = "{:g}".format(sum)
#     print(sum)

# 4056 연말 정산
# n=int(input())
#
# if n<=500:
#     res = n*0.7
# elif n<=1500:
#     res = 350 + (n-500)*0.4
# elif n<=4500:
#     res = 750 + (n-1500)*0.15
# elif n<=10000:
#     res = 1200+(n-4500)*0.05
# else:
#     res = 1475 + (n-10000)*0.02
# res = int(res)
# print(res)

# 4501 백설공주와 난쟁이
# num=[0]*7
#
# for i in range(7):
#     num[i]=int(input())
#
# num=sorted(num)
#
# print(num[6])
# print(num[5])

# 4506 최대공약수와 최소공배수
# a,b=map(int,input().split())
#
# n=max(a,b)
#
# for i in range(n,0,-1):
#     if a%i==0 and b%i==0:
#         print(i)
#         print(i*(a//i)*(b//i))
#         break
