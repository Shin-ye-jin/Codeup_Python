# 4681 검증수
# num=list(map(int,input().split()))
# sum=0
# for i in num:
#     sum+=(i*i)
#
# print(sum%10)

# 4691 주사위 네 개
# n=int(input())
# dice =[]
#
# def f(dice):
#     if len(set(dice))==1:
#         return 50000 + dice[0]*5000
#     elif len(set(dice))==2:
#         if dice[1]==dice[2]:
#             return 10000+dice[3]*1000
#         else:
#             return 2000 + dice[1]*500 + dice[2]*500
#     elif len(set(dice))==3:
#         for i in range(len(dice)):
#             if dice[i]==dice[i+1]:
#                 return 1000 + dice[i]*100
#     else:
#         return dice[3]*100
#
# for i in range(n):
#     num=sorted(list(map(int,input().split())))
#     dice.append(f(num))
#
# print(max(dice))

# 4711 지능형 기차
# a,b=map(int,input().split())
# max,cnt=b,b
# for i in range(3):
#     a,b=map(int,input().split())
#     cnt=cnt-a+b
#     if max<cnt:
#         max=cnt
#
# print(max)

# 4716 지능형 기차 2
# a,b=map(int,input().split())
# max,cnt=b,b
# for i in range(9):
#     a,b=map(int,input().split())
#     cnt=cnt-a+b
#     if max<cnt:
#         max=cnt
#
# print(max)

# 4721 투표
# 4726 수열