P = int(input())
Q = [ int(i) for i in input().split()]
P = len(Q)
U = 0
for Xt in range(0,P-2):
    for Yt in range(Xt+1, P-1):
        for Zt in range(Yt+1, P):
            if Q[Xt] > Q[Yt] > Q[Zt] :
                U =U+ 1
print(U)
