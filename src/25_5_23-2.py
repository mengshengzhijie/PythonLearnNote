"""
Created by MengShengZhiJie 2025/5/23 09:01
"""
from traceback import format_list
from urllib.parse import SplitResult

# Age = 17
# a = 1
# if Age < 18:
#     print("小于18")
# elif Age == 18:
#     print("等于18")
#     if a == 1:
#         print("a等于1")
#     else:
#         print("a不等于1")
# else:
#     print("大于18")
#
# while a < Age :
#     a+=1
#     print(a,end=",")
#
# i = 1
# j = 1
# while i <= 100:
#     i += 1
#     while  i < 100:
#         print(j)
#         j+=j
#         break

Str = "hello word"
for i in Str:
    print(i,end="")
for i in range(1,10,1):
    print(i,end="")
print()
#for i in ranfe(开始，结束，步长)
s = 0
for j in range(1,101):
    s+=j
print(s)