i=int(input())
z=0
x=0
b=[]
while z<90 and z<i:
  s=0
  for j in str(i-z):
    s+=int(j)
  if s+(i-z)==i:
    x+=1
    boh.append(i-z)
  z+=1
print(x)
for z in boh:
  print(z)
