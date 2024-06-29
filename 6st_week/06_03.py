# 1357 삼각형 출력하기 4
# n=int(input())
# for i in range(1,n+1):
#     for j in range(0,i):
#         print('*',end='')
#     print()
# for i in range(n,1,-1):
#     for j in range(1,i):
#         print("*",end='')
#     print()

# 1358 삼각형 출력하기 5
# n=int(input())
# for i in range(0,n//2+1):
#     for j in range(0,n//2-i):
#         print(' ',end='')
#     for j in range(0,i*2+1):
#         print('*',end='')
#     print()

# 1361 별 계단 만들기
n=int(input())
for i in range(0,n):
    for j in range(0,i):
        print(' ',end='')
    for j in range(0,2):
        print('*',end='')
    print()