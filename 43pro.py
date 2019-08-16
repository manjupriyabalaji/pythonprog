import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
b = []
d = []
s = []
for i in range(1,n+1) :
    if i not in L:
        b.append(i)
for i in L :
    if L.count(i) > 1 and i not in d :
        d.append(i)
for i in range(0,n) :
    if L[i] in d :
        s.append(i)
c = len(b)
for i in range(0,n) :
    if len(b) == 0 :
        break
    if i in s :
        if i == s[0] :
            if b[0] < L[i] :
                L[i] = b.pop(0)
                s.pop(0)
            elif L[i] in d :
                s.pop(0)
                d.remove(L[i])
            else :
                L[i] = b.pop(0)
                s.pop(0)


print()
print(*L)
