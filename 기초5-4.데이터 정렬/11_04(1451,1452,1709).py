# 1451 데이터 정렬 (small)
# n=int(input())
# matrix=[0]*n
#
# for i in range(n):
#     num=int(input())
#     matrix[i]=num
#
# matrix.sort()
#
# for i in range(n):
#     print(matrix[i])

# 1452 데이터 정렬 (large)
# n=int(input())
# matrix=[0]*n
#
# for i in range(n):
#     num=int(input())
#     matrix[i]=num
#
# matrix.sort()
#
# for i in range(n):
#     print(matrix[i])

# 1709 내림차순 정렬
n=int(input())
num=list(map(int,input().split()))
num.sort(reverse=True) # 정렬 후 역순으로 배열
for i in num: # 리스트에 있는 모든 요소를 출력
    print(i,end=' ')