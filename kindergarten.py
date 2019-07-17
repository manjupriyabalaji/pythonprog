xt=int(input())
yt=0
zt=[]
for j in range(1,xt+1):
  zt.append(j)
for j in range(len(zt)):
  for j in range(j+1,len(zt)):
    yt+=1
print(yt)
