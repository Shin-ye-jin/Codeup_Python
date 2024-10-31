# 2332 경상북도 시군 이름 0 (스페셜 저지)



# 2333 경상북도 시군 이름 1
# a=input()
# b=input()
#
# if (b in a) == True: # 문자열의 부분일치
#     print("O")
# else:
#     print("X")

# 2334 좋아하는 보석 0 (스페셜 저지)



# 2335 좋아하는 보석 1



# 2336 청송 황금 사과 0 (스페셜 저지)



# 2337 청송 황금 사과 1
from datetime import datetime, timedelta
k=int(input())
n,m=map(int,input().split())
num = k-(m+n)
cnt,x,y=0,0,0
year,month,day = 2023,1,1
while True:
  cnt = 2*x+3*y
  if cnt>=num: break
  x+=2
  y+=3
res = max(x,y)
if num==0: res+=2
else: res+=1
time1 = datetime(year,month,day)
time2 = time1+timedelta(days=res)
print(time2.strftime('%Y'),time2.strftime('%m'),time2.strftime('%d'),sep="/")