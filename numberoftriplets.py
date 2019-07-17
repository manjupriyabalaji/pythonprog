ab=int(input())
s1=list(map(int,input().split()))
c=0
for m in range(ab):
  for n in range(m,ab):
    for o in range(n,ab):
      if(s1[i]<s1[j]<s1[o]):
        d+=1
print(d)
