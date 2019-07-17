import math
ab1,cb1=map(int,input().split())
ccb=[]
bbb=list(map(int,input().split()))
for j in range(0,cb1):
        mm,nn =map(int,input().split())
        ccb.append([mm,nn])
for j in ccb:
        dd=j[0]-1
        ee=j[1]-1
        print(math.gcd(bbb[dd],sss[ee]))
