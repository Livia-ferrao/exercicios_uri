A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
X, Y, Z = input().split()
X = int(X)
Y = int(Y)
Z = int(Z)
maxX = int(X/A)
maxY = int(Y/B)
maxZ = int(Z/C)
print("%d" % int((maxX*maxY*maxZ)))