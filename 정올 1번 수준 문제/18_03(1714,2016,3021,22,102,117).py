# 1714 숫자 거꾸로 출력하기
# n=int(input())
#
# if n==0:
#     print(0)
# else:
#     while n!=0:
#         m = n%10
#         print(m,end='')
#         n=n//10

# 2016 천단위 구분기호
# n=int(input())
# num=list(input())
# res = n%3
#
# for i in range(n):
#     if i>0 and (i%3==res):
#         print(",",end='')
#     print(num[i],end='')

# 3021 큰 수 덧셈
# a=int(input())
# b=int(input())
# print(a+b)

# 3022 큰 수 뺄셈
# a=int(input())
# b=int(input())
# print(a-b)

# 3102 STL stack
# import sys
# import re
#
# n = int(sys.stdin.readline())
#
# class Stack:
#     def __init__(self):  #생성자
#         self.slist = []
#
#     def push(self, x):
#         self.slist.append(x)
#
#     def empty(self):
#         if len(self.slist) == 0:
#             return 'true'
#         else:
#             return 'false'
#
#     def top(self):
#         if self.empty() == 'true':
#             return -1
#         else:
#             return self.slist[-1]
#
#     def pop(self):
#         if self.empty() == 'false':
#             self.slist.pop()
#
#     def size(self):
#         return len(self.slist)
#
# stack = Stack()
# for _ in range(n):
#     i = sys.stdin.readline().rstrip()
#     s = re.split('[()]', i)
#     if s[0] == "push":
#         stack.push(int(s[1]))
#     elif s[0] == "empty":
#         print(stack.empty())
#     elif s[0] == "top":
#         print(stack.top())
#     elif s[0] == "pop":
#         stack.pop()
#     elif s[0] == "size":
#         print(stack.size())

# 3117 0은 빼!