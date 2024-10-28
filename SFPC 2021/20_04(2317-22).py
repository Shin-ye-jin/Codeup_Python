# 2317 산딸기 정렬0 (스페셜 저지)



# 2318 산딸기 정렬1
# m = int(input())
# matrix = list(map(int, input().split()))
# n = int(input())
#
# for i in range(3):
#     for j in range(m):
#         if i == 0 and matrix[j] < n:
#             print(matrix[j], end=' ')
#         if i == 1 and matrix[j] == n:
#             print(matrix[j], end=' ')
#         if i == 2 and matrix[j] > n:
#             print(matrix[j], end=' ')

# 2319 감귤 나무 관리0 (스페셜 저지)


# 2320 감귤 나무 관리1
# import math
#
# a,b=map(int,input().split())
# r = int(input())
# c,d = map(int,input().split())
# c-=a
# d-=b
# re = math.sqrt(c*c+d*d)
#
# if re<r: print("in")
# elif re==r: print("on")
# else:
#   print("out")


# 2321 자녀의 혈액형0 (스페셜 저지)



# 2322 자녀의 혈액형1
a,b=input().split()
matrix1 = list(a)
matrix2 = list(b)
result = []

for i in matrix1:
    for j in matrix2:
        if i+j == "AA" or i+j == "AO" or i+j == "OA":
            result.append("A")
        elif i+j == "BB" or i+j == "BO" or i+j == "OB":
            result.append("B")
        elif i+j == "OO":
            result.append("O")
        elif i+j == "AB" or i+j == "BA":
            result.append("AB")

result = sorted(result)
set = []

for i in result:
    if i not in set:
        set.append(i)

for i in set:
    print(i,end=' ')