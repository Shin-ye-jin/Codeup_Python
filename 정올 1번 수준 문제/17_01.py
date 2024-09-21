# 4011 생년월일 출력
# n=input()
# year = n[0:2]
# month=n[2:4]
# day=n[4:6]
#
# if int(n[7])==1:
#     year = 1900+int(year)
#     print(year,month,day+" M",sep="/")
# elif int(n[7])==2:
#     year = 1900+int(year)
#     print(year,month,day+" F",sep="/")
# elif int(n[7])==3:
#     year = 2000+int(year)
#     print(year,month,day+" M",sep="/")
# elif int(n[7])==4:
#     year = 2000+int(year)
#     print(year,month,day+" F",sep="/")

# 4013 진법 변환
# n=int(input())
#
# b=format(n,'b')
# o=format(n,'o')
# h=format(n,'X')
#
# print("2",b)
# print("8",o)
# print("16",h)

# 4016 세 수의 최대공약수 구하기
# a,b,c=map(int,input().split())
#
# num=min(a,b,c)
#
# for i in range(num,0,-1):
#     if a%i==0 and b%i==0 and c%i==0:
#         print(i)
#         break

# 4021 홀수의 합 구하기
# num=list(map(int,input().split()))
# result,count=0,0
#
# for i in num:
#     if i%2==1:
#         result+=i
#         count+=1
#
# if count==0:
#     print("-1")
# else:
#     print(result)

# 4026 중앙 값
# num=list(map(int,input().split()))
# num=sorted(num)
# print(num[2])

# 4031 가장 큰 수
# num=list(map(int,input().split()))
# num=sorted(num)
# n=len(num)
# a,b=0,0
# for i in range(n-1,-1,-1):
#     if num[i]%2==1:
#         a=num[i]
#         break
#
# for i in range(n-1,-1,-1):
#     if num[i]%2==0:
#         b=num[i]
#         break
#
# print(a+b)
