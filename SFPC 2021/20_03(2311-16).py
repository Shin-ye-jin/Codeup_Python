# 2311 주차 공간0 (스페셜 저지)



# 2312 주차 공간1
# n,a,b=map(int,input().split())
# matrix = [0]*n
# c1,c2=0,0
# n1 = list(map(int,input().split()))
# n2 = list(map(int,input().split()))
#
# for i in n1:
#   matrix[i-1]+=1
# for j in n2:
#   matrix[j-1]+=1
#
# for i in range(n):
#   if matrix[i]==0:
#     c1+=1
#   if matrix[i]==2:
#     c2+=1
#
# print(c1,c2)

# 2313 한라봉 포장0 (스페셜 저지)



# 2314 한라봉 포장1
# matrix=[10,5,3,1]
# n=int(input())
# cnt=0
# for i in matrix:
#   cnt+=n//i
#   n%=i
#
# print(cnt)

# 2315 약수 배수 놀이0 (스페셜 저지)




# 2316 약수 배수 놀이1
# n,m=map(int,input().split())
# matrix=list(map(int,input().split()))
# cnt=0
# for j in matrix:
#   for k in range(m,0,-1):
#     if k%j==0 or j%k==0: cnt+=1
#   print(cnt)
#   cnt=0

