# 2367 야채빵과 단팥빵 1



# 2368 전주 비빔밥 0 (스페셜 저지)



# 2369 전주 비빔밥 1
# a,b,c=map(int,input().split())
# matrix = [a//40, b//50, c//30]
# res = min(matrix)
# print(res)


# 2370 특산물 선물 세트 0 (스페셜 저지)



# 2371 특산물 선물 세트 1
# n=int(input())
# num=list(map(int,input().split()))
# m,k = map(int,input().split())



# 2372 당일치기 전주 여행 0 (스페셜 저지)



# 2373 당일치기 전주 여행 1



# 2374 군산스탬프투어 0(스페셜 저지)



# 2375 군산스탬프투어 1
import math

n,m,k,t = map(int,input().split())
matrix = list(map(int,input().split()))
res = []
cnt,cnt2 = 5,0 # 숙소에서 나가서 숙소로 오니까 5로 시작하고 끝지점에서도 5 더하기!
for i in range(k):
    num = list(map(int,input().split()))
    for j in range(len(num)):
        cnt+=matrix[num[j]-1]
    cnt+=5*m
    res.append(cnt)
    num.clear()
    cnt=5

for i in res:
    if i<=t:
        cnt2+=1

print(cnt2)