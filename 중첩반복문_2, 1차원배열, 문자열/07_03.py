# 1411 빠진 카드
# n=int(input())
# card = list(range(1,n+1))
# num=[]
#
# for i in range(0,n-1):
#     num.append(int(input()))
#
# for i in num:
#     card.remove(i) # card 리스트 내에서 num과 같은 숫자 삭제
#
# print(card[0])

# 1412 알파벳 개수 출력하기
# s=list(range(0,26))
# count='a'
# temp=input()
# num=list(range(0,26))
# for i in range(0,26):
#     num[i]=0
#
# for i in range(0,26):
#     s[i]=count
#     count= chr(ord(count)+1) # 문자 -> 숫자 ord / 숫자 -> 문자 chr
#
# for i in temp:
#     for j in range(0,26):
#         if i==s[j]:
#             num[j]+=1
#
# for i in range(0,26):
#     print("%c:%d"%(s[i],num[i]))

# 1416 2진수 변환
n=int(input())
num=list(range(0,255)) # 메모리 고려하기
i=0
while n>1:
    num[i] = n%2
    i+=1
    n=n//2
num[i]=n
for j in range(i,-1,-1):
    print(num[j],end='')