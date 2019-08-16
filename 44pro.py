bt16,bt26,bt36,b=map(int,input().split())
l=list(map(int,input().split()))
xen=[]
for i in range(0,len(l)):
    for j in range(i,len(l)):
        for k in range(j,len(l)):
            xen.append(bt26*l[i]+bt36*l[j]+b*l[k])
print(max(xen))
