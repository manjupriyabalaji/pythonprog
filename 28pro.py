b=int(input())
n=list(map(int,input().split()))
n.sort()
s=0
ms=0
for i in range(len(n)):
    if npk[i]>=s:
        ms=ms+1
    s=s+n[i]
print(ms)
