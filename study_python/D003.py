# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

test = input()
li = []
for i in range(1,10):
    a = i * int(test)
    li.append(str(a))
print(" ".join(li))