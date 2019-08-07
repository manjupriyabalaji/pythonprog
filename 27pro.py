p,s=map(int,input().split())
z=list(map(int,input().split()))
v=list(map(int,input().split()))
t=[]
u=0
for i in range(p):
    y=v[i]/z[i]
    t.append(y)
while s>=0 and len(t)>0:
    m=t.index(max(t))
    if s>=z[m]:
        u=u+v[m]
        s=s-z[m]
    z.pop(m)
    v.pop(m)
    t.pop(m)
print(u)
