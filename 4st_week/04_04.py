# 1251 1부터 100까지 출력하기
# for i in range(1,101):
#     print(i,end=" ")

# 1252 1부터 n까지 출력하기
# n=int(input())
# for i in range(1,n+1):
#     print(i,end=" ")

# 1253 a부터 b까지 출력하기
# a,b=map(int,input().split())
# if a>b:
#     for b in range(b,a+1):
#         print(b,end=" ")
# elif b>a:
#     for a in range(a,b+1):
#         print(a,end=" ")
# else:
#     for a in range(a,b+1):
#         print(a,end=" ")

# 1254 알파벳 출력하기
# a,b=input().split()
# a=ord(a) # ord 문자 넣으면 해당하는 정수 반환
# b=ord(b)
# for i in range(a,b+1):
#     print(chr(i),end=' ') # chr 숫자를 넣으면 해당하는 문자 반환

# 1255 두 실수 사이 출력하기
# a,b=map(float,input().split())
# while a<=b: # while 사용하기
#     print("%.2f" % a,end=" ")
#     a+=0.01

# 1256 별 출력하기
# a=int(input())
# for i in range(1,a+1):
#     print("*",end="")