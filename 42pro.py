import sys,string


def maxOfSegmentMins(Lact26, nect26, kint26):
    if k == 1:
        return min(Lact26)
    if k == 2 :
        return max(Lact26[0], Lact26[nect26 - 1])
    return max(Lact26)

nect26,k = input().split()
nect26,k = int(nect26),int(k)
Lact26 = [ int(x) for x in input().split()]
nect26 = len(Lact26)
ans = maxOfSegmentMins(Lact26, nect26, k)
print(ans)
