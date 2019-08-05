s=int(input())
b=list(map(int,input().split()))[:s]
z=sum(b[0:s:2])
y=sum(b[1:s:2])
if z>y:
  print(z)
else:
  print(y)
