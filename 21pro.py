man=int(input())
min=list(x(int,input().split()))
a=int(man/2)
r=min[:a]
m=min[a::]
if ((sum(r)//len(r))==(sum(m)//len(m))):
    print("yes")
else:
    print("no")
