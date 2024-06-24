# 1284 암호 해독
# n=int(input())
# num=[]
#
# for i in range(2,n):
#     if n%i==0:
#         num.append(i)
#
# if len(num)==2:
#     if 4 in num:
#         print("wrong number")
#     else:
#         print(*num)
# else:
#     print("wrong number")

# 1285 계산기 2
# a=input()
# num=[]
# count=[]
# for i in range(len(a)):
#     a[i].isdigit()
#     if a[i].isdigit()==True:
#         count.append(a[i])
#     else:
#         num.append(int("".join(count)))
#         count=[]
#         num.append(a[i])
# cnt=1
# result=int(num[0])
# while True:
#     if num[cnt]=='=':
#         break
#     if num[cnt]=='+':
#         cnt+=1
#         result+=int(num[cnt])
#         cnt+=1
#     elif num[cnt]=='-':
#          cnt+=1
#          result-=int(num[cnt])
#          cnt+=1
#     elif num[cnt]=='*':
#          cnt+=1
#          result*=int(num[cnt])
#          cnt+=1
#     elif num[cnt]=='/':
#          cnt+=1
#          result//=int(num[cnt])
#          cnt+=1
#
# print(result)

# 1286 최댓값, 최솟값
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
max=n1
min=n1

if max <n2: max=n2
if max <n3: max=n3
if max <n4: max=n4
if max <n5: max=n5

if min >n2: min=n2
if min >n3: min=n3
if min >n4: min=n4
if min >n5: min=n5

print(max)
print(min)