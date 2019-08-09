n,k=map(int,input().split())
L=list(map(int,input().split()))
C=0
for Xt in L:
    if Xt<=(5-k):
        C+=1
G=C//3
print(G)
