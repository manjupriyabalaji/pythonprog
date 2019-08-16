n=int(input())
l=list(map(int,input().split()))
a=0
b=0
l.sort(reverse=True)
for i in l:
  m=ah+i
  if b>m:
    a=m
  else:
    a=b
    b=m
print(a,b)
