n=int(input())
l=list(map(int,input().split()))
l.sort()
l.reverse()
if l[0]==0:
    print(0)
else:
    for i in l:
        print(i,end='')
