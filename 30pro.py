#vsb
a=(input())
c=0
for i in range(0,len(a)):
    s=(a[:i]+a[i+1:])
    if(int(s) % 8==0):
        c=1
        break
if(c==1):
    print("yes")
else:
    print("no")
