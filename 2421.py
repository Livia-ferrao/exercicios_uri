# -*- coding: utf-8 -*-

x,y = input().split()
x = int(x)
y = int(y)
l1,h1 = input().split()
l1 = int(l1)
h1 = int(h1)
l2,h2 = input().split()
l2 = int(l2)
h2 = int(h2)
if (h1 + h2 <= x and l1 <= y and l2 <= y) or (h1 + l2 <= x and l1 <= y and h2 <= y) or (h2 + l1 <= x and h1 <= y and l2 <= y) or (l1 + l2 <= x and h1 <= y and h2 <= y) or (h1 + h2 <= y and l1 <= x and l2 <= x) or (h1 + l2 <= y and l1 <= x and h2 <= x) or (h2 + l1 <= y and h1 <= x and l2 <= x) or (l1 + l2 <= y and h1 <= x and h2 <= x):
    print("S")
else:
    print("N")