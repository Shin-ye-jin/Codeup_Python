# 1805 입체기동장치 생산공장
# num=[0]*101
# n=int(input())
#
# for i in range(n):
#     a,b=map(int,input().split())
#     num[a]=b+1
#
# for i in range(1,101):
#     if num[i]!=0:
#         print("%d %d"%(i,num[i]-1))

# 3015 성적표 출력
n,m=map(int,input().split())
matrix=[]

for i in range(n):
    name,score=input().split()
    matrix.append([name,int(score)]) # 원소 2개 리스트 추가
matrix.sort(key=lambda x:-x[1]) # 정렬 ( 학생 성적 정렬 등등 알기)

for i in range(m): # name은 첫행
    print(matrix[i][0])


