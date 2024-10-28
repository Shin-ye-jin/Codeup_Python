# 3127 수식 계산 1
# def Cal(x):
#   stack=[]
#   for i in x:
#     if i == '+':
#       stack.append(stack.pop()+stack.pop())
#     elif i == '-':
#       stack.append(-(stack.pop()-stack.pop()))
#     elif i == "*":
#       stack.append(stack.pop()*stack.pop())
#     elif i == '/':
#       divide = stack.pop()
#       stack.append(stack.pop()/divide)
#     else:
#       stack.append(int(i))
#   return stack.pop()
#
# print(Cal(input().split()))

# 3129 올바른 괄호 2
# def check(s):
#     stack = []
#     brackets = {')': '(', '}': '{', ']': '['}
#
#     for c in s:
#         if c in brackets.values():
#             stack.append(c)
#         elif c in brackets.keys():
#             if not stack or brackets[c] != stack.pop():
#                 return False
#         else:
#             continue
#
#     return not stack
#
# input_str = input()
# result = check(input_str)
#
# if result == True:
#     print("good")
# else:
#     print("bad")

# 3130 소들의 헤어스타일
# class Stack:
#     def __init__(self):
#         self.len = 0
#         self.list = []
#
#     def push(self, num):
#         self.list.append(num)
#         self.len += 1
#
#     def pop(self):
#         if self.size() == 0:
#             return -1
#         pop_result = self.list[self.len - 1]
#         del self.list[self.len - 1]
#         self.len -= 1
#
#         return pop_result
#
#     def size(self):
#         return self.len
#
#     def empty(self):
#         return 1 if self.len == 0 else 0
#
#     def top(self):
#         return self.list[-1] if self.size() != 0 else -1
#
#
# n = int(input())
# stack = Stack()
# cnt = 0
#
# for _ in range(n):
#     c = int(input())
#
#     if stack.empty():
#         stack.push(c)
#     elif stack.top() <= c:
#         stack.pop()
#         while stack.top() <= c and stack.top() != -1:
#             stack.pop()
#         stack.push(c)
#     else:
#         stack.push(c)
#
#     cnt += stack.size() - 1
#
# print(cnt)