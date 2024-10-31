# 2361 고창 여행 0 (스페셜 저지)



# 2362 고창 여행 1
# n,k = map(int,input().split())
# matrix = [0]*8
# number= [0,1000,1000,2000,3000,3000,6000,6000]
# sum=0
# for i in range(n):
#     num=list(map(int,input().split()))
#     del num[0]
#     for j in num:
#         matrix[j]+=1
#
# for i in range(8):
#     if matrix[i]>=k:
#         sum+=number[i]
#
# print(sum*n)

# 2363 고추장 항아리 0 (스페셜 저지)




# 2364 고추장 항아리 1
# n=int(input())
# cnt = n//5
# res=0
# if n%5>0: res+=cnt+1
# else: res=cnt
#
# print(res,cnt*150000)


# 2365 고추장 항아리 2
n=int(input())
cnt = n//5
res=0
if n%5>0: res+=cnt+1
else: res=cnt

print(res,cnt*150000)


# 2366 야채빵과 단팥방 0 (스페셜 저지)