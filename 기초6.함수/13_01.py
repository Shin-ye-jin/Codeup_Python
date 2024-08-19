# 1571 [기초-함수작성] 함수로 Upper Bound 위치 리턴하기
def f(n,k):
    for i in range(n):
        if num[i]>k:
            return i+1
    return n+1

n=int(input())
num=list(map(int,input().split()))
k=int(input())

print(f(n,k))

# 1576, 1577 c전용 문제