# -*- coding: utf-8 -*-

teste = 1
while True:
    a, v = [int(i) for i in input().split()]
    if a == v == 0:
        break

    aero = [0] * a
    while v:
        v -= 1
        x, y = [int(i) for i in input().split()]
        aero[x-1] += 1
        aero[y-1] += 1

    m = max(aero)
    maior = ''
    for i in range(len(aero)):
        if aero[i] == m:
            maior += str(i+1) + ' '
    print('Teste %d' % teste)
    teste += 1
    print(maior)
    print("")