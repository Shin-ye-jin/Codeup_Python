# 3004 데이터 재정렬
# n=int(input())
# count = [0 for i in range(500001)]
# num_list=list(map(int,input().split()))
#
# for i in range(n): # 입력 받은 값 위치 기록
#     num = num_list[i]
#     count[num]+=1
#
# for i in range(len(count)-1): # 이전까지의 누적 개수 구하기
#     count[i+1] += count[i]
#
# for i in num_list: # count 배열에 기록되어 있는 값에 따라 인덱스 위치 정하기
#     print(count[i]-1, end=' ')
# 시간 초과로 인해 계수 정렬

# result = sorted(num)
#
# for i in range(n):
#     for j in range(n):
#         if num[i]==result[j]:
#             print(j,end=' ')

# 3011 거품 정렬 (Bubble Sort)
# n=int(input())
# num=list(map(int,input().split()))
# count=0
# number = 0
# for i in range(n-1):
#     for j in range(n-1-i):
#         if num[j]>num[j+1]:
#             temp=num[j]
#             num[j]=num[j+1]
#             num[j+1]=temp
#             count+=1
#
#     if count != 0: # 반복 했으면 +1
#         number += 1
#     count=0 # 초기화
#
# print(number)

# 3014 정렬을 빠르게! - 메모리 초과
n=int(input())
num=list(map(int,input().split()))
count = [0]*100000
number=0
for i in num:
    count[i]+=1

for i in range(100000):
    if count[i]>0:
        for j in range(count[i]):
            print(i,end=' ')
            number+=1
    if number == n:
        break
