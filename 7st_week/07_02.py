# 1402 거꾸로 출력하기 3
# n=int(input())
# num=list(map(int,input().split()))
# for i in range(n-1,-1,-1):
#     print(num[i],end=' ')

# 1403 배열 두번 출력하기
# n=int(input())
# num=list(map(int,input().split()))
# for i in range(0,n):
#     print(num[i])
# for i in range(0,n):
#     print(num[i])

# 1405 숫자 로테이션
# n=int(input())
# num=list(map(int,input().split()))
# index=0
# for z in range(0,n):
#     index=z
#     for j in range(0,n):
#         print(num[index],end=' ')
#         index+=1
#         if index==n:
#             index=0
#     print()

# 1407 문자열 출력하기 1
# temp=list(input().split())
# for i in temp:
#     if i==' ':
#         continue
#     else:
#         print(i,end='')

# 1409 기억력 테스트 1
# num=list(map(int,input().split()))
# n=int(input())
# print(num[n-1])

# 1410 올바른 괄호 1 (괄호 개수 세기)
temp=list(input())
count1=0
count2=0
for i in temp:
    if i == "(":
        count1+=1
    elif i == ")":
        count2+=1
print(count1,count2)