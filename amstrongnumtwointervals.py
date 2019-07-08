a1,a2=map(int,input().split())
for i in range(a1+1,a2):
    b=0
    c=i
    while(b>0):
        d=c%10
        b+=d**3
        c//=10
    if(i==b):
        print(i,end=" ")
