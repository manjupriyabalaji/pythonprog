a,b=c(int,input().split())
d=list(c(int,input().split()))
d.sort()
d.reverse()
x=c
y=0
for j in d:
    if(x>=j):
        z=int(x/j)
        y=y+z
        x=x-z*j
    if x==0:
        break
if(x==0):
   print(y)
else:
   print("it's not posiible to select coins in such a way that they sum upto",c)
