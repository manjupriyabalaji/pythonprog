b,z=map(int,input().split())
skip=[]
for i in range(0,b):
    a=[int(sv) for sv in input().split()]
    skip.append(sorted(a))
for i in range(0,len(skip[0])):
  #print(skip[i])
  for j in range(0,len(skip)-1):
    if skip[j][i]>skip[j+1][i]:
      skip[j][i],skip[j+1][i]=skip[j+1][i],skip[j][i]
for i in skip:
  print(*i)
