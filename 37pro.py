n=int(input())
l=list(map(int,input().split()))
c=0
i=0
while(i<len(l)):
    t=l[i]
    if(i==0):
        if(len(l)==1):
            c=1 
            break
    elif(i==len(l)-1):
        c=c
    else:
        if(t>l[i+1] and t>l[i-1]):
            c=c+1
        elif(t<l[i-1] and t<l[i+1]):
            c=c+1
    i=i+1
print(c)
