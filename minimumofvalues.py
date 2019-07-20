x11,y11=map(int,input().split())
z1=list(map(int,input().split()))
n11=[]
for j in range(y11):
  m,s=map(int,input().split())
  n11=z1[m-1:s]
  print(min(n11))
